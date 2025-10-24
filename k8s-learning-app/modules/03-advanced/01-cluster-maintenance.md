# Module 3.1: Cluster Maintenance and Upgrades

## OS Upgrades and Node Maintenance

### Draining Nodes

Safely evict all pods from a node before maintenance.

```bash
# Drain node (evict pods, mark unschedulable)
kubectl drain <node-name>

# Drain with force (for pods not managed by controllers)
kubectl drain <node-name> --force

# Drain and delete local data
kubectl drain <node-name> --delete-emptydir-data

# Drain and ignore DaemonSets
kubectl drain <node-name> --ignore-daemonsets

# Drain with grace period
kubectl drain <node-name> --grace-period=300

# Complete drain command (common usage)
kubectl drain <node-name> --ignore-daemonsets --delete-emptydir-data --force
```

### Cordoning Nodes

Mark node as unschedulable (doesn't evict existing pods).

```bash
# Cordon node (mark unschedulable)
kubectl cordon <node-name>

# Uncordon node (mark schedulable)
kubectl uncordon <node-name>

# Check node status
kubectl get nodes
```

### Node Maintenance Workflow

```bash
# 1. Drain node
kubectl drain worker-1 --ignore-daemonsets --delete-emptydir-data

# 2. Perform maintenance (SSH to node)
ssh worker-1
sudo apt update && sudo apt upgrade -y
sudo reboot

# 3. Wait for node to come back
kubectl get nodes --watch

# 4. Uncordon node
kubectl uncordon worker-1

# 5. Verify pods rescheduled
kubectl get pods -o wide
```

## Kubernetes Cluster Upgrades

### Upgrade Strategy

- Upgrade one minor version at a time (1.24 -> 1.25 -> 1.26)
- Upgrade master nodes first
- Then upgrade worker nodes
- Test in staging environment first

### Version Compatibility

- kube-apiserver: v1.25
- kubelet: v1.24 or v1.25 (one version behind or same)
- kubectl: v1.24, v1.25, or v1.26 (one version behind or ahead)

### Upgrade Master Node (kubeadm)

```bash
# 1. Check current version
kubectl get nodes
kubeadm version

# 2. Plan upgrade
kubeadm upgrade plan

# 3. Drain master node
kubectl drain master --ignore-daemonsets

# 4. Upgrade kubeadm
apt update
apt-cache madison kubeadm  # View available versions
apt-mark unhold kubeadm
apt-get update && apt-get install -y kubeadm=1.26.0-00
apt-mark hold kubeadm

# 5. Verify kubeadm version
kubeadm version

# 6. Apply upgrade
sudo kubeadm upgrade apply v1.26.0

# 7. Upgrade kubelet and kubectl
apt-mark unhold kubelet kubectl
apt-get update && apt-get install -y kubelet=1.26.0-00 kubectl=1.26.0-00
apt-mark hold kubelet kubectl

# 8. Restart kubelet
sudo systemctl daemon-reload
sudo systemctl restart kubelet

# 9. Uncordon master
kubectl uncordon master

# 10. Verify
kubectl get nodes
```

### Upgrade Worker Nodes (kubeadm)

```bash
# 1. Drain worker node (from master)
kubectl drain worker-1 --ignore-daemonsets --delete-emptydir-data

# 2. SSH to worker node
ssh worker-1

# 3. Upgrade kubeadm
apt-mark unhold kubeadm
apt-get update && apt-get install -y kubeadm=1.26.0-00
apt-mark hold kubeadm

# 4. Upgrade kubelet config
sudo kubeadm upgrade node

# 5. Upgrade kubelet and kubectl
apt-mark unhold kubelet kubectl
apt-get update && apt-get install -y kubelet=1.26.0-00 kubectl=1.26.0-00
apt-mark hold kubelet kubectl

# 6. Restart kubelet
sudo systemctl daemon-reload
sudo systemctl restart kubelet

# 7. Exit worker node
exit

# 8. Uncordon worker (from master)
kubectl uncordon worker-1

# 9. Verify
kubectl get nodes
```

### Rolling Worker Node Upgrades

Upgrade one worker at a time to maintain availability.

```bash
# Upgrade worker-1
kubectl drain worker-1 --ignore-daemonsets --delete-emptydir-data
# ... perform upgrade on worker-1 ...
kubectl uncordon worker-1

# Wait for pods to be stable
kubectl get pods -o wide --watch

# Upgrade worker-2
kubectl drain worker-2 --ignore-daemonsets --delete-emptydir-data
# ... perform upgrade on worker-2 ...
kubectl uncordon worker-2

# Repeat for remaining workers
```

## etcd Backup and Restore

### etcd Backup

```bash
# Check etcd version
ETCDCTL_API=3 etcdctl version

# Backup etcd
ETCDCTL_API=3 etcdctl snapshot save /backup/etcd-snapshot.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# Verify backup
ETCDCTL_API=3 etcdctl snapshot status /backup/etcd-snapshot.db \
  --write-out=table
```

### etcd Restore

```bash
# 1. Stop kube-apiserver
mv /etc/kubernetes/manifests/kube-apiserver.yaml /tmp/

# 2. Restore etcd snapshot
ETCDCTL_API=3 etcdctl snapshot restore /backup/etcd-snapshot.db \
  --data-dir=/var/lib/etcd-restore \
  --initial-cluster=master=https://127.0.0.1:2380 \
  --initial-advertise-peer-urls=https://127.0.0.1:2380

# 3. Update etcd manifest to use new data directory
vi /etc/kubernetes/manifests/etcd.yaml
# Change: --data-dir=/var/lib/etcd-restore

# 4. Restore kube-apiserver
mv /tmp/kube-apiserver.yaml /etc/kubernetes/manifests/

# 5. Verify cluster
kubectl get pods -n kube-system
kubectl get nodes
```

### Automated Backup Script

```bash
#!/bin/bash
# etcd-backup.sh

BACKUP_DIR="/backup/etcd"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/etcd-snapshot-$TIMESTAMP.db"

# Create backup directory
mkdir -p $BACKUP_DIR

# Perform backup
ETCDCTL_API=3 etcdctl snapshot save $BACKUP_FILE \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# Verify backup
ETCDCTL_API=3 etcdctl snapshot status $BACKUP_FILE --write-out=table

# Keep only last 7 backups
find $BACKUP_DIR -name "etcd-snapshot-*.db" -type f -mtime +7 -delete

echo "Backup completed: $BACKUP_FILE"
```

```bash
# Make executable
chmod +x etcd-backup.sh

# Schedule with cron (daily at 2 AM)
crontab -e
0 2 * * * /usr/local/bin/etcd-backup.sh
```

## Certificate Management

### View Certificates

```bash
# Check certificate expiration
kubeadm certs check-expiration

# View certificate details
openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout
```

### Renew Certificates

```bash
# Renew all certificates
kubeadm certs renew all

# Renew specific certificate
kubeadm certs renew apiserver

# Verify renewal
kubeadm certs check-expiration
```

### Manual Certificate Renewal

```bash
# 1. Backup certificates
cp -r /etc/kubernetes/pki /etc/kubernetes/pki.backup

# 2. Renew certificates
kubeadm certs renew all

# 3. Restart control plane components
kubectl -n kube-system delete pod -l component=kube-apiserver
kubectl -n kube-system delete pod -l component=kube-controller-manager
kubectl -n kube-system delete pod -l component=kube-scheduler
kubectl -n kube-system delete pod -l component=etcd

# 4. Update kubeconfig
cp /etc/kubernetes/admin.conf ~/.kube/config

# 5. Verify
kubectl get nodes
```

## High Availability

### HA Control Plane

Multiple master nodes with load balancer.

```
                  Load Balancer
                       |
        +-------------+-------------+
        |             |             |
    Master-1      Master-2      Master-3
        |             |             |
        +-------------+-------------+
                       |
                     etcd
                       |
        +-------------+-------------+
        |             |             |
    Worker-1      Worker-2      Worker-3
```

### Stacked etcd Topology

etcd runs on same nodes as control plane.

### External etcd Topology

etcd runs on separate dedicated nodes.

## Cluster Health Checks

```bash
# Check component status
kubectl get componentstatuses
kubectl get cs

# Check node status
kubectl get nodes
kubectl describe node <node-name>

# Check system pods
kubectl get pods -n kube-system

# Check cluster info
kubectl cluster-info
kubectl cluster-info dump

# Check API server health
curl -k https://localhost:6443/healthz

# Check etcd health
ETCDCTL_API=3 etcdctl endpoint health \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key
```

## CKA Exam Tips

- Know the complete drain workflow: `drain -> maintenance -> uncordon`
- Practice cluster upgrades (master first, then workers)
- Memorize etcd backup and restore commands
- Understand certificate expiration and renewal
- Know difference between drain and cordon
- Practice with `--ignore-daemonsets` and `--delete-emptydir-data` flags
- Understand version compatibility rules
- Know where certificates are located: `/etc/kubernetes/pki/`
- Practice checking component health

## Practice Exercises

1. Drain a worker node
2. Cordon a node
3. Uncordon a node after maintenance
4. Perform etcd backup
5. Restore from etcd backup
6. Check certificate expiration
7. Renew certificates
8. Upgrade kubeadm cluster (practice in lab)
9. Create automated backup script
10. Check cluster health

## Common Issues

```bash
# Node not ready after uncordon
kubectl describe node <node-name>
systemctl status kubelet

# Pods not scheduling after uncordon
kubectl get nodes  # Check node is Ready
kubectl describe node <node-name>  # Check taints

# etcd backup fails
# Check endpoints and certificates paths
# Ensure ETCDCTL_API=3 is set

# Upgrade fails
# Check version compatibility
# Ensure no minor versions are skipped
# Check node is drained properly
```

## Quick Reference

```bash
# Node maintenance
kubectl drain <node> --ignore-daemonsets --delete-emptydir-data
kubectl cordon <node>
kubectl uncordon <node>

# etcd backup
ETCDCTL_API=3 etcdctl snapshot save backup.db \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# etcd restore
ETCDCTL_API=3 etcdctl snapshot restore backup.db --data-dir=/var/lib/etcd-restore

# Certificates
kubeadm certs check-expiration
kubeadm certs renew all

# Upgrade
kubeadm upgrade plan
kubeadm upgrade apply v1.26.0
```

## Next Steps

Move to Module 3.2: Troubleshooting and Debugging

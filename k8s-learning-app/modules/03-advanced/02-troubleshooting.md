# Module 3.2: Troubleshooting and Debugging

## Troubleshooting Methodology

1. **Identify the problem**: What's broken?
2. **Gather information**: Logs, events, status
3. **Analyze**: Find root cause
4. **Fix**: Apply solution
5. **Verify**: Confirm fix works
6. **Document**: Record solution

## Application Failure Troubleshooting

### Pod Issues

#### Pod Stuck in Pending

```bash
# Check pod status
kubectl get pods

# Describe pod for events
kubectl describe pod <pod-name>

# Common causes:
# - Insufficient resources (CPU/Memory)
# - PVC not bound
# - Node selector/affinity not matching
# - Image pull issues
# - No nodes available

# Check node resources
kubectl top nodes
kubectl describe nodes

# Check PVC
kubectl get pvc

# Check events
kubectl get events --sort-by=.metadata.creationTimestamp
```

#### Pod in CrashLoopBackOff

```bash
# Check pod logs
kubectl logs <pod-name>
kubectl logs <pod-name> --previous  # Logs from crashed container

# Check pod events
kubectl describe pod <pod-name>

# Common causes:
# - Application error
# - Missing dependencies
# - Configuration error
# - Liveness probe failing
# - Insufficient permissions

# Debug by running shell
kubectl exec -it <pod-name> -- /bin/sh

# Check container restart count
kubectl get pod <pod-name> -o jsonpath='{.status.containerStatuses[0].restartCount}'
```

#### ImagePullBackOff / ErrImagePull

```bash
# Describe pod
kubectl describe pod <pod-name>

# Common causes:
# - Wrong image name/tag
# - Private registry without imagePullSecret
# - Network issues
# - Registry down

# Verify image exists
docker pull <image-name>

# Check image pull secret
kubectl get secrets
kubectl describe secret <secret-name>

# Create image pull secret
kubectl create secret docker-registry regcred \
  --docker-server=<registry> \
  --docker-username=<user> \
  --docker-password=<pass>
```

#### Pod Evicted

```bash
# Check pod status
kubectl get pods | grep Evicted

# Get eviction reason
kubectl describe pod <pod-name>

# Common causes:
# - Node running out of disk
# - Node running out of memory
# - Node pressure

# Clean up evicted pods
kubectl get pods | grep Evicted | awk '{print $1}' | xargs kubectl delete pod

# Check node conditions
kubectl describe node <node-name> | grep -A 5 Conditions
```

### Service Issues

#### Service Not Accessible

```bash
# Check service exists
kubectl get svc

# Describe service
kubectl describe svc <service-name>

# Check endpoints
kubectl get endpoints <service-name>

# If no endpoints:
# - Check pod labels match service selector
# - Check pods are running
# - Check pod ports match service targetPort

# Verify pod labels
kubectl get pods --show-labels

# Verify service selector
kubectl get svc <service-name> -o yaml | grep selector -A 5

# Test service from within cluster
kubectl run curl --image=curlimages/curl -i --rm --restart=Never -- curl <service-name>:<port>

# Port forward to test
kubectl port-forward svc/<service-name> 8080:80
```

#### DNS Not Working

```bash
# Check CoreDNS/kube-dns
kubectl get pods -n kube-system | grep dns

# Check CoreDNS logs
kubectl logs -n kube-system -l k8s-app=kube-dns

# Test DNS resolution
kubectl run busybox --image=busybox:1.28 --rm -it --restart=Never -- nslookup kubernetes.default

# Check DNS service
kubectl get svc -n kube-system

# Check DNS ConfigMap
kubectl get cm -n kube-system coredns -o yaml
```

## Control Plane Failure

### API Server Issues

```bash
# Check API server pod
kubectl get pods -n kube-system | grep apiserver

# Check API server logs
kubectl logs -n kube-system kube-apiserver-<master>

# If kubectl not working, check directly
docker ps | grep apiserver
docker logs <container-id>

# Check API server process
ps aux | grep kube-apiserver

# Check API server manifest
cat /etc/kubernetes/manifests/kube-apiserver.yaml

# Check certificates
ls -la /etc/kubernetes/pki/
openssl x509 -in /etc/kubernetes/pki/apiserver.crt -text -noout | grep -A 2 Validity

# Check API server health
curl -k https://localhost:6443/healthz
```

### etcd Issues

```bash
# Check etcd pod
kubectl get pods -n kube-system | grep etcd

# Check etcd logs
kubectl logs -n kube-system etcd-<master>

# Check etcd health
ETCDCTL_API=3 etcdctl endpoint health \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# Check etcd members
ETCDCTL_API=3 etcdctl member list \
  --endpoints=https://127.0.0.1:2379 \
  --cacert=/etc/kubernetes/pki/etcd/ca.crt \
  --cert=/etc/kubernetes/pki/etcd/server.crt \
  --key=/etc/kubernetes/pki/etcd/server.key

# Check etcd manifest
cat /etc/kubernetes/manifests/etcd.yaml
```

### Scheduler Issues

```bash
# Check scheduler pod
kubectl get pods -n kube-system | grep scheduler

# Check scheduler logs
kubectl logs -n kube-system kube-scheduler-<master>

# Check scheduler manifest
cat /etc/kubernetes/manifests/kube-scheduler.yaml

# Check for scheduling events
kubectl get events | grep -i scheduler
```

### Controller Manager Issues

```bash
# Check controller manager pod
kubectl get pods -n kube-system | grep controller-manager

# Check controller manager logs
kubectl logs -n kube-system kube-controller-manager-<master>

# Check controller manager manifest
cat /etc/kubernetes/manifests/kube-controller-manager.yaml

# Check for controller events
kubectl get events | grep -i controller
```

## Worker Node Failure

### Node NotReady

```bash
# Check node status
kubectl get nodes

# Describe node
kubectl describe node <node-name>

# Check node conditions
kubectl get node <node-name> -o jsonpath='{.status.conditions[*].type}' | tr ' ' '\n'
kubectl get node <node-name> -o jsonpath='{.status.conditions[?(@.status=="False")].message}'

# Common causes:
# - kubelet not running
# - Network issues
# - Certificate issues
# - Out of resources

# SSH to node and check kubelet
ssh <node>
systemctl status kubelet
journalctl -u kubelet -f

# Check kubelet logs
journalctl -u kubelet -n 100
```

### Kubelet Issues

```bash
# On worker node:

# Check kubelet status
systemctl status kubelet

# Check kubelet logs
journalctl -u kubelet -f
journalctl -u kubelet -n 100 --no-pager

# Check kubelet config
cat /var/lib/kubelet/config.yaml

# Restart kubelet
systemctl restart kubelet

# Check kubelet ports
netstat -tlnp | grep kubelet

# Check kubelet process
ps aux | grep kubelet
```

### Container Runtime Issues

```bash
# Check Docker (if using Docker)
systemctl status docker
docker ps
docker logs <container-id>

# Check containerd
systemctl status containerd
crictl ps
crictl logs <container-id>

# Check CRI-O
systemctl status crio
crictl ps

# Restart container runtime
systemctl restart docker  # or containerd or crio
```

## Network Troubleshooting

### Pod-to-Pod Communication

```bash
# Get pod IPs
kubectl get pods -o wide

# Test connectivity from one pod to another
kubectl exec <pod1> -- ping <pod2-ip>

# Check if network plugin running
kubectl get pods -n kube-system | grep -E 'calico|weave|flannel|cilium'

# Check network plugin logs
kubectl logs -n kube-system <network-pod>

# Check iptables rules (on node)
sudo iptables -L -t nat | grep <service-name>
```

### Service Connectivity

```bash
# Check service and endpoints
kubectl get svc
kubectl get endpoints

# Test service from pod
kubectl run test --image=busybox --rm -it --restart=Never -- wget -O- <service>:<port>

# Check kube-proxy
kubectl get pods -n kube-system | grep proxy
kubectl logs -n kube-system <kube-proxy-pod>

# On node, check kube-proxy mode
kubectl logs -n kube-system <kube-proxy-pod> | grep "Using iptables"

# Check iptables
sudo iptables-save | grep <service-name>
```

### DNS Issues

```bash
# Test DNS from pod
kubectl run busybox --image=busybox:1.28 --rm -it --restart=Never -- nslookup kubernetes.default

# Test external DNS
kubectl run busybox --image=busybox:1.28 --rm -it --restart=Never -- nslookup google.com

# Check CoreDNS ConfigMap
kubectl get cm -n kube-system coredns -o yaml

# Check CoreDNS pods
kubectl get pods -n kube-system -l k8s-app=kube-dns

# Check CoreDNS logs
kubectl logs -n kube-system -l k8s-app=kube-dns

# Restart CoreDNS
kubectl rollout restart deployment coredns -n kube-system
```

## Debugging Tools

### kubectl debug

```bash
# Debug a pod (creates ephemeral container)
kubectl debug <pod-name> -it --image=busybox

# Debug with specific image
kubectl debug <pod-name> -it --image=ubuntu --target=<container-name>

# Create debug copy of pod
kubectl debug <pod-name> -it --copy-to=debug-pod --container=debug

# Debug node
kubectl debug node/<node-name> -it --image=ubuntu
```

### Common Debug Commands

```bash
# Check logs
kubectl logs <pod-name>
kubectl logs <pod-name> -c <container-name>
kubectl logs <pod-name> --previous
kubectl logs <pod-name> -f  # Follow logs
kubectl logs -l app=nginx  # By label

# Execute commands
kubectl exec -it <pod-name> -- /bin/sh
kubectl exec <pod-name> -- cat /etc/resolv.conf
kubectl exec <pod-name> -c <container> -- command

# Port forwarding
kubectl port-forward <pod-name> 8080:80
kubectl port-forward svc/<service-name> 8080:80

# Events
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl get events -w
kubectl get events --field-selector involvedObject.name=<pod-name>

# Resource usage
kubectl top nodes
kubectl top pods
kubectl top pods --containers

# Describe resources
kubectl describe pod <pod-name>
kubectl describe node <node-name>
kubectl describe svc <service-name>
```

### Debugging Networking

```bash
# Network debugging pod
kubectl run netdebug --image=nicolaka/netshoot --rm -it -- /bin/bash

# Inside netdebug pod:
# ping <ip>
# curl <url>
# nslookup <domain>
# dig <domain>
# traceroute <ip>
# netstat -tlnp
# ss -tlnp
```

## Performance Issues

### High CPU/Memory Usage

```bash
# Check resource usage
kubectl top nodes
kubectl top pods --all-namespaces
kubectl top pods --containers

# Identify top consumers
kubectl top pods --all-namespaces --sort-by=cpu
kubectl top pods --all-namespaces --sort-by=memory

# Check resource requests/limits
kubectl describe pod <pod-name> | grep -A 5 Limits

# Check node capacity
kubectl describe node <node-name> | grep -A 5 Capacity
kubectl describe node <node-name> | grep -A 5 Allocated

# Check OOM kills
dmesg | grep -i oom
journalctl -k | grep -i oom
```

### Slow Application Response

```bash
# Check pod readiness
kubectl get pods
kubectl describe pod <pod-name> | grep -A 10 Conditions

# Check probes
kubectl describe pod <pod-name> | grep -A 5 Liveness
kubectl describe pod <pod-name> | grep -A 5 Readiness

# Check application logs
kubectl logs <pod-name> -f

# Check resource constraints
kubectl top pod <pod-name>

# Check for throttling (on node)
cat /sys/fs/cgroup/cpu/kubepods/*/cpu.stat
```

## CKA Exam Tips

- Follow systematic troubleshooting approach
- Start with `kubectl get` and `kubectl describe`
- Check logs: `kubectl logs`
- Check events: `kubectl get events`
- Know where to find manifests: `/etc/kubernetes/manifests/`
- Know where to find logs: `journalctl -u kubelet`
- Practice common failure scenarios
- Be familiar with `kubectl debug`
- Know how to check certificates and their expiration
- Practice troubleshooting without internet access

## Practice Exercises

1. Troubleshoot pod in CrashLoopBackOff
2. Fix ImagePullBackOff error
3. Troubleshoot service not accessible
4. Fix DNS resolution issues
5. Troubleshoot node NotReady
6. Fix kubelet issues
7. Troubleshoot pod-to-pod connectivity
8. Debug API server issues
9. Troubleshoot etcd problems
10. Identify and fix resource exhaustion

## Troubleshooting Checklist

### Pod Issues
- [ ] Check pod status: `kubectl get pods`
- [ ] Describe pod: `kubectl describe pod`
- [ ] Check logs: `kubectl logs`
- [ ] Check events: `kubectl get events`
- [ ] Check resources: `kubectl top pod`

### Service Issues
- [ ] Check service: `kubectl get svc`
- [ ] Check endpoints: `kubectl get endpoints`
- [ ] Verify pod labels match selector
- [ ] Test connectivity from pod

### Node Issues
- [ ] Check node status: `kubectl get nodes`
- [ ] Describe node: `kubectl describe node`
- [ ] SSH to node
- [ ] Check kubelet: `systemctl status kubelet`
- [ ] Check logs: `journalctl -u kubelet`

### Control Plane Issues
- [ ] Check control plane pods: `kubectl get pods -n kube-system`
- [ ] Check component logs
- [ ] Check manifests: `/etc/kubernetes/manifests/`
- [ ] Check certificates
- [ ] Check ports and connectivity

## Quick Reference

```bash
# Basic troubleshooting
kubectl get pods
kubectl describe pod <pod>
kubectl logs <pod>
kubectl logs <pod> --previous
kubectl exec -it <pod> -- /bin/sh

# Events and status
kubectl get events --sort-by=.metadata.creationTimestamp
kubectl get componentstatuses
kubectl cluster-info

# Node troubleshooting
kubectl get nodes
kubectl describe node <node>
kubectl top nodes

# Service troubleshooting
kubectl get svc
kubectl get endpoints
kubectl describe svc <service>

# Control plane
kubectl get pods -n kube-system
journalctl -u kubelet -f
/etc/kubernetes/manifests/
```

## Next Steps

Move to CKA Exam Preparation Guide

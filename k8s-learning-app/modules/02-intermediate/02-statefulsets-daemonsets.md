# Module 2.2: StatefulSets and DaemonSets

## StatefulSets

StatefulSets manage stateful applications that require stable network identities and persistent storage.

### When to Use StatefulSets

- Applications requiring stable network identifiers
- Applications needing ordered deployment and scaling
- Applications requiring stable persistent storage
- Databases, message queues, distributed systems

### StatefulSet vs Deployment

| Feature | StatefulSet | Deployment |
|---------|------------|------------|
| Pod naming | Predictable (web-0, web-1) | Random hash |
| Pod identity | Stable | Ephemeral |
| Storage | Per-pod persistent volumes | Shared storage |
| Startup | Ordered (sequential) | Parallel |
| Scaling | Ordered | Random |
| Use case | Stateful apps | Stateless apps |

### StatefulSet YAML

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-headless
spec:
  clusterIP: None  # Headless service required
  selector:
    app: nginx
  ports:
  - port: 80
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: nginx-headless
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
        ports:
        - containerPort: 80
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
```

### StatefulSet Features

#### 1. Stable Network Identity

Pods get predictable names: `<statefulset-name>-<ordinal>`
- web-0
- web-1
- web-2

DNS entries: `<pod-name>.<service-name>.<namespace>.svc.cluster.local`
- web-0.nginx-headless.default.svc.cluster.local
- web-1.nginx-headless.default.svc.cluster.local

#### 2. Ordered Operations

**Deployment**: Pods created sequentially (0, 1, 2, ...)
**Scaling Up**: New pods created one at a time
**Scaling Down**: Pods terminated in reverse order
**Updates**: Rolling update in reverse ordinal order

#### 3. Persistent Storage

Each pod gets its own PVC from volumeClaimTemplates.
PVCs persist even if StatefulSet is deleted.

### Managing StatefulSets

```bash
# Create StatefulSet
kubectl apply -f statefulset.yaml

# Get StatefulSets
kubectl get statefulsets
kubectl get sts

# Describe StatefulSet
kubectl describe sts web

# Get pods
kubectl get pods -l app=nginx

# Scale StatefulSet
kubectl scale sts web --replicas=5

# Delete StatefulSet (keep PVCs)
kubectl delete sts web

# Delete StatefulSet and PVCs
kubectl delete sts web
kubectl delete pvc www-web-0 www-web-1 www-web-2

# Update strategy
kubectl patch sts web -p '{"spec":{"updateStrategy":{"type":"RollingUpdate"}}}'
```

### Update Strategies

#### 1. RollingUpdate (Default)

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 0  # Update all pods >= this ordinal
```

#### 2. OnDelete

Pods updated only when manually deleted.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  updateStrategy:
    type: OnDelete
```

### Partition Updates

Update only specific pods:

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      partition: 2  # Only update pods with ordinal >= 2
```

Pods web-2 and web-3 updated, web-0 and web-1 remain unchanged.

### StatefulSet with Init Container

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: nginx
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      initContainers:
      - name: init
        image: busybox
        command:
        - sh
        - -c
        - |
          echo "Initializing pod $HOSTNAME" > /work-dir/index.html
        volumeMounts:
        - name: www
          mountPath: /work-dir
      containers:
      - name: nginx
        image: nginx
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
```

## DaemonSets

DaemonSet ensures a copy of a pod runs on all (or selected) nodes.

### When to Use DaemonSets

- Node monitoring agents (Prometheus Node Exporter)
- Log collection agents (Fluentd, Filebeat)
- Storage daemons (Ceph, GlusterFS)
- Network plugins (Calico, Weave)
- Security agents

### DaemonSet YAML

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
  namespace: kube-system
spec:
  selector:
    matchLabels:
      name: fluentd
  template:
    metadata:
      labels:
        name: fluentd
    spec:
      containers:
      - name: fluentd
        image: fluentd:latest
        resources:
          limits:
            memory: 200Mi
          requests:
            cpu: 100m
            memory: 200Mi
        volumeMounts:
        - name: varlog
          mountPath: /var/log
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
```

### DaemonSet Features

- One pod per node (by default)
- Automatically schedules pod on new nodes
- Removes pod when node is removed
- Can target specific nodes using nodeSelector or affinity

### Node Selection

#### Using nodeSelector

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: monitoring-agent
spec:
  selector:
    matchLabels:
      app: monitoring
  template:
    metadata:
      labels:
        app: monitoring
    spec:
      nodeSelector:
        monitoring: "true"  # Only on nodes with this label
      containers:
      - name: agent
        image: monitoring-agent:latest
```

Label nodes:
```bash
kubectl label nodes worker-1 monitoring=true
kubectl label nodes worker-2 monitoring=true
```

#### Using Node Affinity

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: ssd-storage
spec:
  selector:
    matchLabels:
      app: storage
  template:
    metadata:
      labels:
        app: storage
    spec:
      affinity:
        nodeAffinity:
          requiredDuringSchedulingIgnoredDuringExecution:
            nodeSelectorTerms:
            - matchExpressions:
              - key: disk-type
                operator: In
                values:
                - ssd
      containers:
      - name: storage
        image: storage-daemon:latest
```

### Managing DaemonSets

```bash
# Get DaemonSets
kubectl get daemonsets
kubectl get ds
kubectl get ds -n kube-system

# Describe DaemonSet
kubectl describe ds fluentd

# Get pods managed by DaemonSet
kubectl get pods -l name=fluentd

# Delete DaemonSet
kubectl delete ds fluentd

# Update DaemonSet
kubectl set image ds/fluentd fluentd=fluentd:v2
kubectl rollout status ds/fluentd
```

### Update Strategy

#### 1. RollingUpdate (Default)

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
spec:
  updateStrategy:
    type: RollingUpdate
    rollingUpdate:
      maxUnavailable: 1  # Max pods updated at once
```

#### 2. OnDelete

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: fluentd
spec:
  updateStrategy:
    type: OnDelete  # Manual update
```

### Tolerations

DaemonSets often need to run on all nodes including master.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: monitoring
spec:
  selector:
    matchLabels:
      app: monitoring
  template:
    metadata:
      labels:
        app: monitoring
    spec:
      tolerations:
      - key: node-role.kubernetes.io/master
        effect: NoSchedule
      - key: node-role.kubernetes.io/control-plane
        effect: NoSchedule
      containers:
      - name: monitoring
        image: monitoring:latest
```

## CKA Exam Tips

### StatefulSets
- Know when to use StatefulSet vs Deployment
- Understand ordered deployment and scaling
- Practice creating StatefulSets with volumeClaimTemplates
- Know update strategies (RollingUpdate, OnDelete, partition)
- Understand stable network identities
- Be able to troubleshoot StatefulSet issues

### DaemonSets
- Know use cases for DaemonSets
- Practice node selection with nodeSelector and affinity
- Understand tolerations for running on master nodes
- Know update strategies
- Be quick with `kubectl get ds` commands

## Practice Exercises

### StatefulSets
1. Create a StatefulSet with 3 replicas
2. Verify stable network identities
3. Check PVCs created for each pod
4. Scale StatefulSet to 5 replicas
5. Update image and watch rolling update
6. Use partition to update only specific pods
7. Delete and recreate StatefulSet
8. Verify PVCs persist

### DaemonSets
1. Create a DaemonSet
2. Verify pod on each node
3. Add node and verify DaemonSet schedules pod
4. Use nodeSelector to target specific nodes
5. Add tolerations for master nodes
6. Update DaemonSet image
7. Watch rolling update

## Troubleshooting

```bash
# StatefulSet pods not starting
kubectl describe sts <name>
kubectl get pods -l app=<label>
kubectl describe pod <pod-name>
kubectl get pvc  # Check PVCs

# DaemonSet not running on all nodes
kubectl get nodes  # Check node status
kubectl describe ds <name>  # Check events
kubectl get nodes --show-labels  # Verify nodeSelector labels
kubectl describe node <node>  # Check taints
```

## Quick Reference

```bash
# StatefulSet
kubectl get sts
kubectl describe sts <name>
kubectl scale sts <name> --replicas=5
kubectl rollout status sts/<name>
kubectl delete sts <name> --cascade=orphan  # Keep pods

# DaemonSet
kubectl get ds
kubectl get ds -n kube-system
kubectl describe ds <name>
kubectl set image ds/<name> container=image:tag
kubectl rollout status ds/<name>
```

## Next Steps

Move to Module 2.3: Jobs and CronJobs

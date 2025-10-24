# Module 2.1: Storage - Volumes, PV, and PVC

## Volumes Overview

Kubernetes volumes solve two problems:
1. Data persistence beyond container lifecycle
2. Data sharing between containers in a pod

## Volume Types

### 1. emptyDir

Temporary storage, deleted when pod is removed.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: emptydir-pod
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: cache
      mountPath: /cache
  volumes:
  - name: cache
    emptyDir: {}
```

Use cases:
- Temporary scratch space
- Cache data
- Sharing data between containers in same pod

### 2. hostPath

Mounts file/directory from host node.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: hostpath-pod
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: host-volume
      mountPath: /data
  volumes:
  - name: host-volume
    hostPath:
      path: /var/data
      type: DirectoryOrCreate
```

**Warning**: Use with caution. Pods can access host filesystem.

### 3. configMap and secret

Already covered in Module 1.6.

## Persistent Volumes (PV)

PersistentVolume is a piece of storage in the cluster provisioned by admin or dynamically using Storage Classes.

### PV YAML

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: pv-storage
spec:
  capacity:
    storage: 10Gi
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: manual
  hostPath:
    path: /mnt/data
```

### Access Modes

- **ReadWriteOnce (RWO)**: Volume mounted read-write by single node
- **ReadOnlyMany (ROX)**: Volume mounted read-only by many nodes
- **ReadWriteMany (RWX)**: Volume mounted read-write by many nodes
- **ReadWriteOncePod (RWOP)**: Volume mounted read-write by single pod

### Reclaim Policies

- **Retain**: Manual reclamation (data preserved)
- **Delete**: Volume deleted when PVC is deleted
- **Recycle**: Basic scrub (deprecated)

## Persistent Volume Claims (PVC)

PVC is a request for storage by a user.

### PVC YAML

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: pvc-storage
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi
  storageClassName: manual
```

### Using PVC in Pod

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: pvc-pod
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: storage
      mountPath: /usr/share/nginx/html
  volumes:
  - name: storage
    persistentVolumeClaim:
      claimName: pvc-storage
```

## Storage Classes

StorageClass provides dynamic provisioning of PersistentVolumes.

### Storage Class YAML

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: fast-storage
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
  fsType: ext4
reclaimPolicy: Delete
allowVolumeExpansion: true
volumeBindingMode: WaitForFirstConsumer
```

### Provisioners

- AWS: `kubernetes.io/aws-ebs`
- GCP: `kubernetes.io/gce-pd`
- Azure: `kubernetes.io/azure-disk`
- NFS: `nfs-client-provisioner`
- Local: `kubernetes.io/no-provisioner`

### Dynamic Provisioning

```yaml
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: dynamic-pvc
spec:
  accessModes:
  - ReadWriteOnce
  storageClassName: fast-storage
  resources:
    requests:
      storage: 10Gi
```

When this PVC is created, a PV is automatically provisioned.

## Volume Snapshots

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot
metadata:
  name: snapshot-1
spec:
  volumeSnapshotClassName: csi-snapshot-class
  source:
    persistentVolumeClaimName: pvc-storage
```

## CSI (Container Storage Interface)

Modern way to integrate external storage systems.

Benefits:
- Vendor-neutral
- Out-of-tree plugins
- Standardized interface

## Storage Commands

```bash
# Get PersistentVolumes
kubectl get pv
kubectl describe pv pv-storage

# Get PersistentVolumeClaims
kubectl get pvc
kubectl describe pvc pvc-storage

# Get StorageClasses
kubectl get sc
kubectl get storageclass
kubectl describe sc fast-storage

# Delete PVC
kubectl delete pvc pvc-storage

# Patch PV reclaim policy
kubectl patch pv pv-storage -p '{"spec":{"persistentVolumeReclaimPolicy":"Retain"}}'
```

## PV and PVC Lifecycle

1. **Provisioning**: PV created (static or dynamic)
2. **Binding**: PVC bound to PV
3. **Using**: Pod uses PVC
4. **Reclaiming**: PVC deleted, PV reclaimed based on policy

### PV Status

- **Available**: Free, not yet bound
- **Bound**: Bound to PVC
- **Released**: PVC deleted, but not yet reclaimed
- **Failed**: Automatic reclamation failed

## Volume Expansion

```yaml
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: expandable
provisioner: kubernetes.io/aws-ebs
allowVolumeExpansion: true  # Enable expansion
```

```bash
# Expand PVC
kubectl edit pvc pvc-storage
# Increase spec.resources.requests.storage

# Check status
kubectl get pvc pvc-storage --watch
```

## StatefulSet Storage

StatefulSets use VolumeClaimTemplates for automatic PVC creation.

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
      storageClassName: fast-storage
      resources:
        requests:
          storage: 1Gi
```

## Local Persistent Volumes

```yaml
apiVersion: v1
kind: PersistentVolume
metadata:
  name: local-pv
spec:
  capacity:
    storage: 100Gi
  volumeMode: Filesystem
  accessModes:
  - ReadWriteOnce
  persistentVolumeReclaimPolicy: Retain
  storageClassName: local-storage
  local:
    path: /mnt/disks/ssd1
  nodeAffinity:
    required:
      nodeSelectorTerms:
      - matchExpressions:
        - key: kubernetes.io/hostname
          operator: In
          values:
          - worker-node-1
```

## CKA Exam Tips

- Understand the relationship: Pod -> PVC -> PV -> Storage Class
- Know access modes and when to use each
- Practice creating PV and PVC with different configurations
- Understand dynamic vs static provisioning
- Know reclaim policies
- Practice troubleshooting storage issues
- Be quick with `kubectl get pv,pvc` commands
- Understand volume binding modes

## Practice Exercises

1. Create a PersistentVolume with hostPath
2. Create a PersistentVolumeClaim
3. Verify PVC is bound to PV
4. Create pod that uses the PVC
5. Write data to the volume and verify persistence
6. Create StorageClass for dynamic provisioning
7. Create PVC with StorageClass
8. Expand a PVC
9. Create StatefulSet with volumeClaimTemplates

## Troubleshooting

```bash
# PVC stuck in Pending
kubectl describe pvc <pvc-name>  # Check events
kubectl get pv  # Check available PVs

# No matching PV
# - Check storage size
# - Check access modes
# - Check storage class name

# Pod can't mount volume
kubectl describe pod <pod-name>  # Check events
kubectl get pvc  # Verify PVC is bound
```

## Quick Reference

```yaml
# PV
apiVersion: v1
kind: PersistentVolume
metadata:
  name: my-pv
spec:
  capacity:
    storage: 10Gi
  accessModes:
  - ReadWriteOnce
  hostPath:
    path: /data

# PVC
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: my-pvc
spec:
  accessModes:
  - ReadWriteOnce
  resources:
    requests:
      storage: 5Gi

# Pod with PVC
volumes:
- name: storage
  persistentVolumeClaim:
    claimName: my-pvc
```

## Next Steps

Move to Module 2.2: StatefulSets and DaemonSets

# Module 1.3: Pods - The Building Blocks

## What is a Pod?

A Pod is the smallest deployable unit in Kubernetes. It represents a single instance of a running process in your cluster.

## Pod Characteristics

- Contains one or more containers (usually one)
- Shares network namespace (same IP address)
- Shares storage volumes
- Scheduled together on the same node
- Ephemeral (not designed to be long-lived)

## Creating Pods

### Method 1: Imperative (Command Line)

```bash
# Create a simple nginx pod
kubectl run nginx-pod --image=nginx

# Create pod with port exposed
kubectl run nginx-pod --image=nginx --port=80

# Create pod and expose as service
kubectl run nginx-pod --image=nginx --port=80 --expose

# Dry run (generate YAML)
kubectl run nginx-pod --image=nginx --dry-run=client -o yaml
```

### Method 2: Declarative (YAML)

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx-pod
  labels:
    app: nginx
    tier: frontend
spec:
  containers:
  - name: nginx
    image: nginx:1.21
    ports:
    - containerPort: 80
```

Save as `pod.yaml` and create:
```bash
kubectl apply -f pod.yaml
```

## Multi-Container Pods

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
spec:
  containers:
  - name: nginx
    image: nginx:1.21
    ports:
    - containerPort: 80
  - name: sidecar
    image: busybox
    command: ['sh', '-c', 'while true; do echo "Sidecar running"; sleep 10; done']
```

## Pod Lifecycle

1. **Pending**: Pod accepted but not yet running
2. **Running**: Pod bound to node, containers running
3. **Succeeded**: All containers terminated successfully
4. **Failed**: At least one container failed
5. **Unknown**: Pod state cannot be determined

## Managing Pods

```bash
# Get pods
kubectl get pods
kubectl get pods -o wide
kubectl get pods -o yaml
kubectl get pods --watch

# Describe pod (detailed info)
kubectl describe pod <pod-name>

# Get pod logs
kubectl logs <pod-name>
kubectl logs <pod-name> -c <container-name>  # for multi-container
kubectl logs <pod-name> --previous  # logs from previous instance

# Execute commands in pod
kubectl exec <pod-name> -- <command>
kubectl exec -it <pod-name> -- /bin/bash

# Port forwarding
kubectl port-forward <pod-name> 8080:80

# Delete pod
kubectl delete pod <pod-name>
kubectl delete pod <pod-name> --force --grace-period=0
```

## Pod Design Patterns

### 1. Sidecar Pattern
Helper container enhances main container (logging, monitoring)

### 2. Ambassador Pattern
Proxy container handles connections to external services

### 3. Adapter Pattern
Standardizes output from main container

## Init Containers

Containers that run before main containers start.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: init-demo
spec:
  initContainers:
  - name: init-service
    image: busybox
    command: ['sh', '-c', 'echo Initializing... && sleep 5']
  containers:
  - name: main
    image: nginx
```

## Resource Requests and Limits

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-pod
spec:
  containers:
  - name: nginx
    image: nginx
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```

## Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: env-pod
spec:
  containers:
  - name: nginx
    image: nginx
    env:
    - name: ENV_VAR
      value: "production"
    - name: SECRET_KEY
      valueFrom:
        secretKeyRef:
          name: my-secret
          key: password
```

## CKA Exam Tips

- Be fast with `kubectl run` for quick pod creation
- Know how to generate YAML: `--dry-run=client -o yaml`
- Practice editing pods (delete and recreate vs. replace)
- Understand pod lifecycle and troubleshooting
- Know how to check logs and exec into pods

## Practice Exercises

1. Create a pod with nginx image
2. Get pod details in YAML format
3. View pod logs
4. Execute a command inside the pod
5. Create a multi-container pod
6. Create a pod with resource limits
7. Delete the pod

## Common Issues and Troubleshooting

```bash
# Pod stuck in Pending
kubectl describe pod <pod-name>  # Check events

# Pod in CrashLoopBackOff
kubectl logs <pod-name>  # Check logs
kubectl describe pod <pod-name>  # Check restart count

# ImagePullBackOff
kubectl describe pod <pod-name>  # Check image name and registry
```

## Next Steps

Move to Module 1.4: ReplicaSets and Deployments

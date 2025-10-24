# Module 1.4: ReplicaSets and Deployments

## ReplicaSets

A ReplicaSet ensures a specified number of pod replicas are running at any time.

### ReplicaSet YAML

```yaml
apiVersion: apps/v1
kind: ReplicaSet
metadata:
  name: nginx-replicaset
  labels:
    app: nginx
spec:
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
```

### Managing ReplicaSets

```bash
# Create ReplicaSet
kubectl apply -f replicaset.yaml

# Get ReplicaSets
kubectl get rs
kubectl get replicaset

# Scale ReplicaSet
kubectl scale rs nginx-replicaset --replicas=5

# Delete ReplicaSet
kubectl delete rs nginx-replicaset
```

## Deployments

Deployments provide declarative updates for Pods and ReplicaSets. They are the recommended way to deploy applications.

### Why Deployments?

- **Rolling updates**: Update pods gradually
- **Rollback**: Revert to previous versions
- **Scaling**: Easy scale up/down
- **Self-healing**: Replace failed pods
- **Version history**: Track deployment revisions

### Deployment YAML

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
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
```

### Creating Deployments

```bash
# Imperative - Quick creation
kubectl create deployment nginx --image=nginx --replicas=3

# Generate YAML
kubectl create deployment nginx --image=nginx --replicas=3 --dry-run=client -o yaml > deployment.yaml

# Declarative - Apply YAML
kubectl apply -f deployment.yaml
```

### Managing Deployments

```bash
# Get deployments
kubectl get deployments
kubectl get deploy
kubectl get deploy -o wide

# Describe deployment
kubectl describe deployment nginx-deployment

# Get deployment details
kubectl get deployment nginx-deployment -o yaml
```

### Scaling Deployments

```bash
# Scale using kubectl scale
kubectl scale deployment nginx-deployment --replicas=5

# Scale using edit
kubectl edit deployment nginx-deployment

# Autoscaling
kubectl autoscale deployment nginx-deployment --min=3 --max=10 --cpu-percent=80
```

### Updating Deployments

```bash
# Update image (rolling update)
kubectl set image deployment/nginx-deployment nginx=nginx:1.22

# Edit deployment
kubectl edit deployment nginx-deployment

# Update using apply
# Edit deployment.yaml then:
kubectl apply -f deployment.yaml

# Rollout status
kubectl rollout status deployment/nginx-deployment
```

### Rolling Updates Strategy

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  strategy:
    type: RollingUpdate
    rollingUpdate:
      maxSurge: 1        # Max pods above desired count
      maxUnavailable: 1  # Max pods unavailable during update
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
```

### Recreate Strategy

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  strategy:
    type: Recreate  # All pods terminated before new ones created
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
```

### Rollback

```bash
# View rollout history
kubectl rollout history deployment/nginx-deployment

# View specific revision
kubectl rollout history deployment/nginx-deployment --revision=2

# Rollback to previous version
kubectl rollout undo deployment/nginx-deployment

# Rollback to specific revision
kubectl rollout undo deployment/nginx-deployment --to-revision=2

# Pause rollout
kubectl rollout pause deployment/nginx-deployment

# Resume rollout
kubectl rollout resume deployment/nginx-deployment
```

### Deployment Status

```bash
# Check rollout status
kubectl rollout status deployment/nginx-deployment

# Get events
kubectl get events --sort-by=.metadata.creationTimestamp

# Watch deployment
kubectl get deployment nginx-deployment --watch
```

## Labels and Selectors

Labels are key-value pairs attached to objects. Selectors filter objects by labels.

```yaml
metadata:
  labels:
    app: nginx
    environment: production
    tier: frontend
```

```bash
# Get pods by label
kubectl get pods -l app=nginx
kubectl get pods -l environment=production
kubectl get pods -l 'environment in (production, staging)'

# Add label
kubectl label pod nginx-pod version=v1

# Remove label
kubectl label pod nginx-pod version-

# Update label
kubectl label pod nginx-pod version=v2 --overwrite
```

## Annotations

Annotations are metadata that tools and libraries can use.

```yaml
metadata:
  annotations:
    description: "Frontend nginx web server"
    maintainer: "devops-team@company.com"
```

## CKA Exam Tips

- Quickly create deployments: `kubectl create deployment`
- Generate YAML for editing: `--dry-run=client -o yaml`
- Know rollout commands by heart
- Practice scaling and updating deployments
- Understand the difference between ReplicaSets and Deployments
- Use `kubectl explain deployment.spec.strategy` for help

## Practice Exercises

1. Create a deployment with 3 replicas of nginx
2. Scale the deployment to 5 replicas
3. Update the image to nginx:1.22
4. Check rollout status
5. View rollout history
6. Rollback to previous version
7. Create deployment with Recreate strategy
8. Practice with labels and selectors

## Common Commands Reference

```bash
# Create
kubectl create deployment myapp --image=nginx --replicas=3

# Get
kubectl get deploy
kubectl get rs
kubectl get pods

# Scale
kubectl scale deployment myapp --replicas=5

# Update
kubectl set image deployment/myapp nginx=nginx:1.22

# Rollout
kubectl rollout status deployment/myapp
kubectl rollout history deployment/myapp
kubectl rollout undo deployment/myapp

# Delete
kubectl delete deployment myapp
```

## Next Steps

Move to Module 1.5: Services and Networking

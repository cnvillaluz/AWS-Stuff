# Module 1.5: Services and Networking

## What is a Service?

A Service is an abstraction that defines a logical set of Pods and a policy to access them. Services provide stable network endpoints for pods.

## Why Services?

- Pods are ephemeral (can be replaced)
- Pod IPs change when recreated
- Services provide stable IP and DNS name
- Load balance traffic across multiple pods
- Service discovery within cluster

## Service Types

### 1. ClusterIP (Default)

Exposes service on internal cluster IP. Only accessible within cluster.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-service
spec:
  type: ClusterIP
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80          # Service port
    targetPort: 80    # Container port
```

```bash
# Create ClusterIP service
kubectl expose deployment nginx-deployment --port=80 --target-port=80

# Access service (from within cluster)
kubectl run busybox --image=busybox --rm -it -- wget -O- nginx-service:80
```

### 2. NodePort

Exposes service on each node's IP at a static port (30000-32767).

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-nodeport
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30080   # Optional, auto-assigned if not specified
```

```bash
# Create NodePort service
kubectl expose deployment nginx-deployment --type=NodePort --port=80

# Access service
# http://<NodeIP>:30080
```

### 3. LoadBalancer

Creates external load balancer (cloud providers only).

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-loadbalancer
spec:
  type: LoadBalancer
  selector:
    app: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

```bash
# Create LoadBalancer service
kubectl expose deployment nginx-deployment --type=LoadBalancer --port=80

# Get external IP
kubectl get service nginx-loadbalancer
```

### 4. ExternalName

Maps service to external DNS name.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: external-service
spec:
  type: ExternalName
  externalName: api.example.com
```

## Service Discovery

### Environment Variables

Kubernetes automatically creates environment variables for services.

```bash
# Format:
<SERVICE_NAME>_SERVICE_HOST
<SERVICE_NAME>_SERVICE_PORT
```

### DNS

Kubernetes DNS automatically creates DNS records for services.

```bash
# Format:
<service-name>.<namespace>.svc.cluster.local

# Examples:
nginx-service.default.svc.cluster.local
database.production.svc.cluster.local
```

## Endpoints

Endpoints track the IP addresses of pods that match the service selector.

```bash
# Get endpoints
kubectl get endpoints
kubectl get ep

# Describe endpoints
kubectl describe endpoints nginx-service
```

## Headless Services

Services without cluster IP. Returns pod IPs directly.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-headless
spec:
  clusterIP: None    # Headless service
  selector:
    app: nginx
  ports:
  - port: 80
```

Use cases:
- StatefulSets
- Direct pod-to-pod communication
- Custom load balancing

## Service with Session Affinity

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx-sticky
spec:
  selector:
    app: nginx
  sessionAffinity: ClientIP  # Sticky sessions
  sessionAffinityConfig:
    clientIP:
      timeoutSeconds: 10800
  ports:
  - port: 80
```

## Multi-Port Services

```yaml
apiVersion: v1
kind: Service
metadata:
  name: multi-port-service
spec:
  selector:
    app: myapp
  ports:
  - name: http
    protocol: TCP
    port: 80
    targetPort: 8080
  - name: https
    protocol: TCP
    port: 443
    targetPort: 8443
```

## Service Commands

```bash
# Create service
kubectl create service clusterip nginx --tcp=80:80
kubectl expose deployment nginx --port=80 --target-port=80

# Get services
kubectl get services
kubectl get svc
kubectl get svc -o wide

# Describe service
kubectl describe service nginx-service

# Get service endpoints
kubectl get endpoints nginx-service

# Delete service
kubectl delete service nginx-service

# Edit service
kubectl edit service nginx-service
```

## Testing Services

```bash
# Port-forward to service
kubectl port-forward service/nginx-service 8080:80

# Access in browser or curl
curl localhost:8080

# Test from within cluster
kubectl run curl --image=curlimages/curl -i --rm --restart=Never -- curl nginx-service:80

# DNS testing
kubectl run busybox --image=busybox --rm -it -- nslookup nginx-service
```

## Ingress (Introduction)

Ingress manages external access to services (HTTP/HTTPS routing).

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: nginx-ingress
spec:
  rules:
  - host: example.com
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: nginx-service
            port:
              number: 80
```

## Network Policies (Introduction)

Control traffic flow between pods.

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-nginx
spec:
  podSelector:
    matchLabels:
      app: nginx
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 80
```

## CKA Exam Tips

- Know all service types and when to use each
- Practice creating services imperatively and declaratively
- Understand selectors and how services find pods
- Know DNS naming convention: `<service>.<namespace>.svc.cluster.local`
- Practice port-forwarding for testing
- Understand the difference between port and targetPort
- Know how to troubleshoot service connectivity

## Practice Exercises

1. Create a deployment with 3 nginx pods
2. Expose it as ClusterIP service
3. Test service connectivity from another pod
4. Change service type to NodePort
5. Create a headless service
6. Create multi-port service
7. Test DNS resolution for services
8. Practice with selectors and labels

## Common Issues

```bash
# Service not routing traffic
kubectl get endpoints <service-name>  # Check if endpoints exist
kubectl describe service <service-name>  # Check selector

# Can't access service
kubectl get svc  # Verify service exists
kubectl describe svc <service-name>  # Check ports and selector
kubectl get pods --show-labels  # Verify pod labels match selector

# DNS not working
kubectl get svc -n kube-system  # Check kube-dns/coredns is running
kubectl run busybox --image=busybox --rm -it -- nslookup kubernetes.default
```

## Quick Reference

```bash
# Create service from deployment
kubectl expose deployment myapp --port=80 --type=ClusterIP

# Create NodePort service
kubectl expose deployment myapp --port=80 --type=NodePort

# Create LoadBalancer service
kubectl expose deployment myapp --port=80 --type=LoadBalancer

# Get service details
kubectl get svc myapp -o yaml

# Test service
kubectl port-forward svc/myapp 8080:80
```

## Next Steps

Move to Module 1.6: ConfigMaps and Secrets

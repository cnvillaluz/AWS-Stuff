# Module 2.4: RBAC and Security

## Role-Based Access Control (RBAC)

RBAC regulates access to Kubernetes resources based on roles assigned to users.

## Core Concepts

### 1. ServiceAccount

Identity for processes running in pods.

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: my-service-account
  namespace: default
```

```bash
# Create ServiceAccount
kubectl create serviceaccount my-sa

# Get ServiceAccounts
kubectl get serviceaccounts
kubectl get sa

# Describe ServiceAccount
kubectl describe sa my-sa
```

### 2. Role

Defines permissions within a namespace.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: pod-reader
  namespace: default
rules:
- apiGroups: [""]  # "" for core API group
  resources: ["pods"]
  verbs: ["get", "list", "watch"]
```

### 3. ClusterRole

Defines permissions cluster-wide.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: secret-reader
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "list"]
```

### 4. RoleBinding

Binds Role to subjects (users, groups, ServiceAccounts) in a namespace.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: read-pods
  namespace: default
subjects:
- kind: ServiceAccount
  name: my-service-account
  namespace: default
roleRef:
  kind: Role
  name: pod-reader
  apiGroup: rbac.authorization.k8s.io
```

### 5. ClusterRoleBinding

Binds ClusterRole cluster-wide.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: read-secrets-global
subjects:
- kind: ServiceAccount
  name: my-service-account
  namespace: default
roleRef:
  kind: ClusterRole
  name: secret-reader
  apiGroup: rbac.authorization.k8s.io
```

## API Groups and Resources

```yaml
rules:
- apiGroups: [""]  # Core API group
  resources: ["pods", "services", "configmaps", "secrets"]
  verbs: ["get", "list", "create", "update", "delete"]

- apiGroups: ["apps"]
  resources: ["deployments", "statefulsets", "daemonsets"]
  verbs: ["get", "list", "create", "update", "patch", "delete"]

- apiGroups: ["batch"]
  resources: ["jobs", "cronjobs"]
  verbs: ["get", "list", "create"]

- apiGroups: ["networking.k8s.io"]
  resources: ["networkpolicies", "ingresses"]
  verbs: ["get", "list"]
```

## Verbs (Permissions)

Common verbs:
- **get**: Read single resource
- **list**: List resources
- **watch**: Watch for changes
- **create**: Create resources
- **update**: Update entire resource
- **patch**: Partially update resource
- **delete**: Delete resource
- **deletecollection**: Delete multiple resources

## Creating Roles

### Imperative Commands

```bash
# Create Role
kubectl create role pod-reader \
  --verb=get,list,watch \
  --resource=pods

# Create ClusterRole
kubectl create clusterrole secret-reader \
  --verb=get,list \
  --resource=secrets

# Create RoleBinding
kubectl create rolebinding read-pods \
  --role=pod-reader \
  --serviceaccount=default:my-service-account

# Create ClusterRoleBinding
kubectl create clusterrolebinding read-secrets \
  --clusterrole=secret-reader \
  --serviceaccount=default:my-service-account
```

## Complete RBAC Example

```yaml
# ServiceAccount
apiVersion: v1
kind: ServiceAccount
metadata:
  name: app-sa
  namespace: production
---
# Role
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: app-role
  namespace: production
rules:
- apiGroups: [""]
  resources: ["pods", "services", "configmaps"]
  verbs: ["get", "list", "watch"]
- apiGroups: ["apps"]
  resources: ["deployments"]
  verbs: ["get", "list", "watch", "update", "patch"]
---
# RoleBinding
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: app-binding
  namespace: production
subjects:
- kind: ServiceAccount
  name: app-sa
  namespace: production
roleRef:
  kind: Role
  name: app-role
  apiGroup: rbac.authorization.k8s.io
---
# Pod using ServiceAccount
apiVersion: v1
kind: Pod
metadata:
  name: app-pod
  namespace: production
spec:
  serviceAccountName: app-sa
  containers:
  - name: app
    image: myapp:latest
```

## Resource Names

Restrict access to specific resource names.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: specific-configmap-reader
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  resourceNames: ["app-config", "db-config"]  # Only these ConfigMaps
  verbs: ["get"]
```

## Aggregated ClusterRoles

Combine multiple ClusterRoles.

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: monitoring
  labels:
    rbac.example.com/aggregate-to-monitoring: "true"
rules:
- apiGroups: [""]
  resources: ["pods", "nodes"]
  verbs: ["get", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: monitoring-aggregate
aggregationRule:
  clusterRoleSelectors:
  - matchLabels:
      rbac.example.com/aggregate-to-monitoring: "true"
rules: []  # Rules automatically filled
```

## Testing RBAC

### kubectl auth can-i

```bash
# Check current user permissions
kubectl auth can-i create deployments
kubectl auth can-i delete pods
kubectl auth can-i get secrets --namespace=kube-system

# Check as specific user
kubectl auth can-i get pods --as=system:serviceaccount:default:my-sa

# Check as user in namespace
kubectl auth can-i create deployments --as=jane --namespace=production

# List all permissions
kubectl auth can-i --list
kubectl auth can-i --list --as=system:serviceaccount:default:my-sa
```

### Impersonation

```bash
# Run command as specific service account
kubectl get pods --as=system:serviceaccount:default:my-sa

# Run as user
kubectl get pods --as=jane --as-group=developers
```

## Default Roles

Kubernetes provides default ClusterRoles:

- **cluster-admin**: Super user access
- **admin**: Namespace admin
- **edit**: Read/write access in namespace
- **view**: Read-only access

```bash
# View default roles
kubectl get clusterroles

# Use default role
kubectl create rolebinding developer-edit \
  --clusterrole=edit \
  --serviceaccount=default:developer-sa \
  --namespace=development
```

## Security Context

Control security settings for pods and containers.

### Pod Security Context

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: security-pod
spec:
  securityContext:
    runAsUser: 1000
    runAsGroup: 3000
    fsGroup: 2000
    runAsNonRoot: true
  containers:
  - name: app
    image: nginx
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        drop:
        - ALL
        add:
        - NET_BIND_SERVICE
      readOnlyRootFilesystem: true
```

### Security Context Options

```yaml
securityContext:
  runAsUser: 1000              # Run as UID 1000
  runAsGroup: 3000             # Primary GID
  runAsNonRoot: true           # Reject if runs as root
  fsGroup: 2000                # Volume ownership GID
  supplementalGroups: [4000, 5000]  # Additional groups
  allowPrivilegeEscalation: false   # No privilege escalation
  readOnlyRootFilesystem: true      # Read-only root filesystem
  privileged: false            # Not privileged
  capabilities:                # Linux capabilities
    add: ["NET_ADMIN"]
    drop: ["ALL"]
  seLinuxOptions:              # SELinux options
    level: "s0:c123,c456"
```

## Network Policies

Control traffic between pods.

### Default Deny All

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: default-deny-all
  namespace: production
spec:
  podSelector: {}  # Apply to all pods
  policyTypes:
  - Ingress
  - Egress
```

### Allow Ingress

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-frontend
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
```

### Allow Egress

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: allow-dns
spec:
  podSelector: {}
  policyTypes:
  - Egress
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          name: kube-system
    ports:
    - protocol: UDP
      port: 53
```

## Pod Security Standards

### Privileged (No restrictions)

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: privileged-ns
  labels:
    pod-security.kubernetes.io/enforce: privileged
```

### Baseline (Minimal restrictions)

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: baseline-ns
  labels:
    pod-security.kubernetes.io/enforce: baseline
    pod-security.kubernetes.io/audit: baseline
    pod-security.kubernetes.io/warn: baseline
```

### Restricted (Highly restricted)

```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: restricted-ns
  labels:
    pod-security.kubernetes.io/enforce: restricted
```

## CKA Exam Tips

- Know how to create Roles, RoleBindings, ClusterRoles, ClusterRoleBindings
- Practice imperative commands for RBAC
- Understand difference between Role and ClusterRole
- Know common API groups and resources
- Master `kubectl auth can-i` for testing permissions
- Practice creating ServiceAccounts and binding them
- Understand security contexts
- Know basic network policies
- Be quick with `kubectl create role/rolebinding` commands

## Practice Exercises

1. Create ServiceAccount for an application
2. Create Role with read permissions for pods
3. Bind Role to ServiceAccount
4. Test permissions with `kubectl auth can-i`
5. Create ClusterRole for reading secrets
6. Create ClusterRoleBinding
7. Create pod with custom ServiceAccount
8. Test ServiceAccount permissions
9. Create Role with resource names restriction
10. Implement pod security context
11. Create Network Policy
12. Use impersonation to test permissions

## Troubleshooting

```bash
# Check RBAC errors
kubectl get events

# View role permissions
kubectl describe role <role-name>
kubectl describe clusterrole <clusterrole-name>

# Check bindings
kubectl get rolebindings
kubectl get clusterrolebindings
kubectl describe rolebinding <binding-name>

# Test permissions
kubectl auth can-i <verb> <resource> --as=<user/sa>
```

## Quick Reference

```bash
# ServiceAccount
kubectl create sa mysa
kubectl get sa

# Role
kubectl create role myrole --verb=get,list --resource=pods
kubectl get roles

# RoleBinding
kubectl create rolebinding mybinding --role=myrole --serviceaccount=default:mysa
kubectl get rolebindings

# ClusterRole
kubectl create clusterrole myclusterrole --verb=get,list --resource=nodes
kubectl get clusterroles

# ClusterRoleBinding
kubectl create clusterrolebinding myclusterbinding --clusterrole=myclusterrole --serviceaccount=default:mysa
kubectl get clusterrolebindings

# Test permissions
kubectl auth can-i create pods
kubectl auth can-i delete deployments --as=system:serviceaccount:default:mysa
kubectl auth can-i --list
```

## Next Steps

Move to Module 3: Advanced Topics

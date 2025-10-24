# Module 1.6: ConfigMaps and Secrets

## ConfigMaps

ConfigMaps store non-confidential configuration data as key-value pairs.

### Why ConfigMaps?

- Decouple configuration from container images
- Make applications portable
- Easy to update without rebuilding images
- Store environment-specific configurations

### Creating ConfigMaps

#### 1. From Literal Values

```bash
kubectl create configmap app-config \
  --from-literal=APP_ENV=production \
  --from-literal=LOG_LEVEL=info \
  --from-literal=MAX_CONNECTIONS=100
```

#### 2. From File

```bash
# Create config file
echo "database_url=postgres://localhost:5432" > config.properties
echo "cache_enabled=true" >> config.properties

# Create ConfigMap from file
kubectl create configmap app-config --from-file=config.properties
```

#### 3. From Directory

```bash
# Create ConfigMap from all files in directory
kubectl create configmap app-config --from-file=./config/
```

#### 4. From YAML

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  APP_ENV: production
  LOG_LEVEL: info
  database_url: postgres://localhost:5432
  config.json: |
    {
      "feature_flag": true,
      "max_retries": 3
    }
```

### Using ConfigMaps in Pods

#### 1. Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: config-pod
spec:
  containers:
  - name: app
    image: nginx
    env:
    - name: APP_ENV
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: APP_ENV
    - name: LOG_LEVEL
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: LOG_LEVEL
```

#### 2. All Keys as Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: config-pod
spec:
  containers:
  - name: app
    image: nginx
    envFrom:
    - configMapRef:
        name: app-config
```

#### 3. Volume Mount

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: config-pod
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
  volumes:
  - name: config-volume
    configMap:
      name: app-config
```

#### 4. Specific Keys as Files

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: config-pod
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
  volumes:
  - name: config-volume
    configMap:
      name: app-config
      items:
      - key: config.json
        path: app-config.json
```

### ConfigMap Commands

```bash
# Get ConfigMaps
kubectl get configmaps
kubectl get cm

# Describe ConfigMap
kubectl describe configmap app-config

# View ConfigMap data
kubectl get configmap app-config -o yaml

# Edit ConfigMap
kubectl edit configmap app-config

# Delete ConfigMap
kubectl delete configmap app-config
```

## Secrets

Secrets store sensitive information like passwords, tokens, and keys.

### Types of Secrets

1. **Opaque**: Generic secret (default)
2. **kubernetes.io/service-account-token**: Service account token
3. **kubernetes.io/dockerconfigjson**: Docker registry credentials
4. **kubernetes.io/tls**: TLS certificate and key
5. **kubernetes.io/ssh-auth**: SSH credentials
6. **kubernetes.io/basic-auth**: Basic authentication

### Creating Secrets

#### 1. From Literal Values

```bash
kubectl create secret generic db-secret \
  --from-literal=username=admin \
  --from-literal=password=secretpass123
```

#### 2. From Files

```bash
echo -n 'admin' > username.txt
echo -n 'secretpass123' > password.txt

kubectl create secret generic db-secret \
  --from-file=username=username.txt \
  --from-file=password=password.txt
```

#### 3. From YAML (Base64 Encoded)

```bash
# Encode values
echo -n 'admin' | base64  # YWRtaW4=
echo -n 'secretpass123' | base64  # c2VjcmV0cGFzczEyMw==
```

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
data:
  username: YWRtaW4=
  password: c2VjcmV0cGFzczEyMw==
```

#### 4. String Data (Not Encoded)

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: db-secret
type: Opaque
stringData:
  username: admin
  password: secretpass123
```

### Docker Registry Secret

```bash
kubectl create secret docker-registry regcred \
  --docker-server=registry.example.com \
  --docker-username=user \
  --docker-password=pass \
  --docker-email=user@example.com
```

### TLS Secret

```bash
kubectl create secret tls tls-secret \
  --cert=path/to/tls.cert \
  --key=path/to/tls.key
```

### Using Secrets in Pods

#### 1. Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-pod
spec:
  containers:
  - name: app
    image: nginx
    env:
    - name: DB_USERNAME
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: username
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-secret
          key: password
```

#### 2. All Keys as Environment Variables

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-pod
spec:
  containers:
  - name: app
    image: nginx
    envFrom:
    - secretRef:
        name: db-secret
```

#### 3. Volume Mount

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-pod
spec:
  containers:
  - name: app
    image: nginx
    volumeMounts:
    - name: secret-volume
      mountPath: /etc/secrets
      readOnly: true
  volumes:
  - name: secret-volume
    secret:
      secretName: db-secret
```

#### 4. Image Pull Secret

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: private-pod
spec:
  containers:
  - name: app
    image: registry.example.com/private-image:latest
  imagePullSecrets:
  - name: regcred
```

### Secret Commands

```bash
# Get secrets
kubectl get secrets

# Describe secret (doesn't show values)
kubectl describe secret db-secret

# View secret (base64 encoded)
kubectl get secret db-secret -o yaml

# Decode secret
kubectl get secret db-secret -o jsonpath='{.data.password}' | base64 --decode

# Edit secret
kubectl edit secret db-secret

# Delete secret
kubectl delete secret db-secret
```

## ConfigMap vs Secret

| Feature | ConfigMap | Secret |
|---------|-----------|--------|
| Purpose | Non-sensitive config | Sensitive data |
| Storage | Plain text | Base64 encoded |
| Size limit | 1MB | 1MB |
| Use cases | Config files, env vars | Passwords, tokens, keys |
| Mounted as | Read/write | Read-only (recommended) |

## Best Practices

### ConfigMaps

- Use for non-sensitive configuration only
- Version your ConfigMaps (add version suffix)
- Update deployments when ConfigMap changes
- Use separate ConfigMaps per environment

### Secrets

- Never commit secrets to Git
- Use external secret management (Vault, AWS Secrets Manager)
- Limit secret access with RBAC
- Rotate secrets regularly
- Use separate secrets per application
- Consider encryption at rest
- Use immutable secrets when possible

## Immutable ConfigMaps/Secrets

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
immutable: true  # Cannot be updated
data:
  APP_ENV: production
```

Benefits:
- Protects from accidental updates
- Improves performance (no watching needed)
- Forces version control (create new ConfigMap)

## CKA Exam Tips

- Know how to create ConfigMaps/Secrets quickly with kubectl
- Practice mounting as environment variables vs volumes
- Understand base64 encoding/decoding
- Know the difference between data and stringData in Secrets
- Practice creating Docker registry secrets
- Be fast with `kubectl create` commands
- Know how to decode secrets: `kubectl get secret <name> -o jsonpath='{.data.key}' | base64 -d`

## Practice Exercises

1. Create ConfigMap from literal values
2. Create ConfigMap from file
3. Mount ConfigMap as environment variables
4. Mount ConfigMap as volume
5. Create Secret from literal values
6. Use Secret in pod as environment variable
7. Create Docker registry secret
8. Create TLS secret
9. Decode a secret value
10. Create immutable ConfigMap

## Quick Reference

```bash
# ConfigMap
kubectl create cm myconfig --from-literal=key=value
kubectl create cm myconfig --from-file=config.txt
kubectl get cm
kubectl describe cm myconfig

# Secret
kubectl create secret generic mysecret --from-literal=password=secret
kubectl create secret docker-registry regcred --docker-server=xxx
kubectl create secret tls tls-secret --cert=tls.crt --key=tls.key
kubectl get secrets
kubectl get secret mysecret -o jsonpath='{.data.password}' | base64 -d
```

## Next Steps

Move to Module 1.7: Namespaces and Resource Quotas

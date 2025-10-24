# Module 1.2: Setting Up Kubernetes Environment

## Installation Options

### 1. Minikube (Local Development)

Minikube runs a single-node Kubernetes cluster on your local machine.

```bash
# Install Minikube (Linux)
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Start Minikube
minikube start

# Check status
minikube status
```

### 2. kubeadm (Production-ready Cluster)

kubeadm is the official tool for creating Kubernetes clusters.

```bash
# Install kubeadm, kubelet, kubectl (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install -y apt-transport-https ca-certificates curl

curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-archive-keyring.gpg

echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list

sudo apt-get update
sudo apt-get install -y kubelet kubeadm kubectl
sudo apt-mark hold kubelet kubeadm kubectl
```

### 3. Kind (Kubernetes in Docker)

```bash
# Install Kind
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

# Create cluster
kind create cluster --name learning-cluster
```

## Installing kubectl

kubectl is the command-line tool for interacting with Kubernetes clusters.

```bash
# Linux
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

# Verify installation
kubectl version --client
```

## Configuring kubectl

```bash
# View current configuration
kubectl config view

# Get contexts
kubectl config get-contexts

# Switch context
kubectl config use-context <context-name>

# Set namespace
kubectl config set-context --current --namespace=<namespace>
```

## Essential kubectl Commands

```bash
# Cluster info
kubectl cluster-info
kubectl get nodes

# Get resources
kubectl get pods
kubectl get services
kubectl get deployments

# Describe resources
kubectl describe node <node-name>
kubectl describe pod <pod-name>

# Create resources
kubectl create -f <file.yaml>
kubectl apply -f <file.yaml>

# Delete resources
kubectl delete pod <pod-name>
kubectl delete -f <file.yaml>

# Logs and debugging
kubectl logs <pod-name>
kubectl exec -it <pod-name> -- /bin/bash
```

## CKA Exam Environment

For the CKA exam:
- You'll work with pre-configured clusters
- kubectl and other tools are already installed
- You need to be fast with kubectl commands
- Practice with command-line only (no GUI)

## Practice Exercise

1. Install Minikube or Kind on your local machine
2. Create a cluster
3. Verify cluster is running: `kubectl get nodes`
4. Explore the cluster: `kubectl get all --all-namespaces`
5. Practice switching contexts and namespaces

## Useful Aliases

```bash
# Add to ~/.bashrc or ~/.zshrc
alias k=kubectl
alias kgp='kubectl get pods'
alias kgs='kubectl get services'
alias kgn='kubectl get nodes'
alias kdp='kubectl describe pod'
alias kaf='kubectl apply -f'
alias kdf='kubectl delete -f'

# Enable kubectl autocompletion
source <(kubectl completion bash)
complete -F __start_kubectl k
```

## Next Steps

Move to Module 1.3: Pods - The Building Blocks

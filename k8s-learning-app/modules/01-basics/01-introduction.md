# Module 1.1: Introduction to Kubernetes

## What is Kubernetes?

Kubernetes (K8s) is an open-source container orchestration platform that automates the deployment, scaling, and management of containerized applications.

## Why Kubernetes?

- **Container Orchestration**: Manages containers across multiple hosts
- **High Availability**: Ensures applications run without downtime
- **Scalability**: Automatically scales applications based on demand
- **Self-healing**: Restarts failed containers automatically
- **Load Balancing**: Distributes traffic across containers
- **Rolling Updates**: Updates applications without downtime

## Kubernetes Architecture

### Master Node Components (Control Plane)

1. **kube-apiserver**:
   - Front-end for the Kubernetes control plane
   - Exposes the Kubernetes API
   - All communications go through the API server

2. **etcd**:
   - Distributed key-value store
   - Stores all cluster data
   - Source of truth for cluster state

3. **kube-scheduler**:
   - Assigns pods to nodes
   - Considers resource requirements, constraints, and policies

4. **kube-controller-manager**:
   - Runs controller processes
   - Node Controller, Replication Controller, Endpoints Controller, etc.

5. **cloud-controller-manager** (optional):
   - Integrates with cloud provider APIs
   - Manages cloud-specific resources

### Worker Node Components

1. **kubelet**:
   - Agent running on each node
   - Ensures containers are running in pods
   - Reports node status to master

2. **kube-proxy**:
   - Network proxy on each node
   - Maintains network rules
   - Enables pod-to-pod communication

3. **Container Runtime**:
   - Software for running containers (Docker, containerd, CRI-O)

## Key Concepts

- **Pod**: Smallest deployable unit, contains one or more containers
- **Node**: Worker machine (VM or physical) that runs pods
- **Cluster**: Set of nodes running containerized applications
- **Namespace**: Virtual cluster for resource isolation
- **Service**: Abstraction for accessing pods
- **Volume**: Directory accessible to containers in a pod

## CKA Exam Focus Areas

For the CKA exam, you need to understand:
- Kubernetes architecture components
- How components communicate
- Role of each component
- Basic cluster operations

## Hands-on Exercise

1. Draw the Kubernetes architecture
2. Explain the role of each component
3. Describe the flow when you create a pod

## Next Steps

Move to Module 1.2: Setting Up Kubernetes Environment

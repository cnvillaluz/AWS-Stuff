# Certified Kubernetes Administrator (CKA) Exam Preparation Guide

## Exam Overview

### Exam Details
- **Duration**: 2 hours
- **Format**: Performance-based, hands-on
- **Passing Score**: 66%
- **Cost**: $395 (includes one free retake)
- **Validity**: 3 years
- **Environment**: Remote proctored or testing center
- **Kubernetes Version**: Check current version on CNCF website

### Exam Format
- 15-20 performance-based tasks
- Real Kubernetes clusters
- Command-line only (no GUI)
- Browser-based terminal
- Online documentation allowed (kubernetes.io)
- No external resources or notes

## Exam Domains and Weights

### 1. Storage (10%)
- Understand storage classes, persistent volumes
- Understand volume mode, access modes and reclaim policies
- Understand persistent volume claims primitive
- Know how to configure applications with persistent storage

### 2. Troubleshooting (30%)
- Evaluate cluster and node logging
- Understand how to monitor applications
- Manage container stdout & stderr logs
- Troubleshoot application failure
- Troubleshoot cluster component failure
- Troubleshoot networking

### 3. Workloads & Scheduling (15%)
- Understand deployments and how to perform rolling updates
- Use ConfigMaps and Secrets to configure applications
- Know how to scale applications
- Understand the primitives used to create robust, self-healing application deployments
- Understand how resource limits can affect Pod scheduling
- Awareness of manifest management and common templating tools

### 4. Cluster Architecture, Installation & Configuration (25%)
- Manage role-based access control (RBAC)
- Use Kubeadm to install a basic cluster
- Manage a highly-available Kubernetes cluster
- Provision underlying infrastructure to deploy a Kubernetes cluster
- Perform a version upgrade on a Kubernetes cluster using Kubeadm
- Implement etcd backup and restore

### 5. Services & Networking (20%)
- Understand host networking configuration on the cluster nodes
- Understand connectivity between Pods
- Understand ClusterIP, NodePort, LoadBalancer service types and endpoints
- Know how to use Ingress controllers and Ingress resources
- Know how to configure and use CoreDNS
- Choose an appropriate container network interface plugin

## Study Plan

### Week 1-2: Fundamentals
- [ ] Kubernetes architecture
- [ ] kubectl commands
- [ ] Pods, ReplicaSets, Deployments
- [ ] Services (ClusterIP, NodePort, LoadBalancer)
- [ ] Namespaces
- [ ] Labels and Selectors

### Week 3-4: Intermediate Concepts
- [ ] ConfigMaps and Secrets
- [ ] Persistent Volumes and PVCs
- [ ] Storage Classes
- [ ] StatefulSets
- [ ] DaemonSets
- [ ] Jobs and CronJobs

### Week 5-6: Advanced Topics
- [ ] RBAC (Roles, RoleBindings, ClusterRoles, ClusterRoleBindings)
- [ ] Network Policies
- [ ] Security Contexts
- [ ] Resource Quotas and LimitRanges
- [ ] Taints and Tolerations
- [ ] Node Affinity

### Week 7-8: Cluster Management
- [ ] Cluster installation with kubeadm
- [ ] Cluster upgrades
- [ ] etcd backup and restore
- [ ] Certificate management
- [ ] Node maintenance (drain, cordon)
- [ ] High availability

### Week 9-10: Troubleshooting
- [ ] Application failure troubleshooting
- [ ] Control plane failure troubleshooting
- [ ] Worker node failure troubleshooting
- [ ] Network troubleshooting
- [ ] Log analysis

### Week 11-12: Practice
- [ ] Timed practice exams
- [ ] Killer.sh practice exam (included with registration)
- [ ] Speed optimization
- [ ] Documentation practice

## Essential kubectl Commands

### Speed Shortcuts
```bash
# Set up aliases
alias k=kubectl
alias kgp='kubectl get pods'
alias kgs='kubectl get svc'
alias kd='kubectl describe'
alias kaf='kubectl apply -f'

# Enable bash completion
source <(kubectl completion bash)
complete -F __start_kubectl k

# Set namespace context
kubectl config set-context --current --namespace=<namespace>

# Use short names
k get po          # pods
k get svc         # services
k get deploy      # deployments
k get rs          # replicasets
k get cm          # configmaps
k get pv          # persistentvolumes
k get pvc         # persistentvolumeclaims
k get ns          # namespaces
```

### Quick Resource Creation
```bash
# Dry run to generate YAML
kubectl run nginx --image=nginx --dry-run=client -o yaml > pod.yaml
kubectl create deployment nginx --image=nginx --dry-run=client -o yaml > deploy.yaml
kubectl expose pod nginx --port=80 --dry-run=client -o yaml > svc.yaml

# Quick imperative commands
kubectl run pod-name --image=image-name
kubectl create deployment deploy-name --image=image --replicas=3
kubectl expose deployment deploy-name --port=80 --target-port=8080
kubectl create configmap cm-name --from-literal=key=value
kubectl create secret generic secret-name --from-literal=password=pass
kubectl create job job-name --image=busybox -- echo "hello"
kubectl create cronjob cj-name --image=busybox --schedule="*/5 * * * *" -- echo "hello"
```

### Essential Commands
```bash
# Get resources
kubectl get all
kubectl get pods -o wide
kubectl get pods --all-namespaces
kubectl get pods --show-labels
kubectl get pods -l app=nginx

# Describe resources
kubectl describe pod <pod-name>
kubectl describe node <node-name>

# Logs
kubectl logs <pod-name>
kubectl logs <pod-name> -f
kubectl logs <pod-name> --previous

# Execute
kubectl exec -it <pod-name> -- /bin/bash

# Edit resources
kubectl edit pod <pod-name>
kubectl set image deployment/nginx nginx=nginx:1.22

# Scale
kubectl scale deployment nginx --replicas=5

# Delete
kubectl delete pod <pod-name>
kubectl delete -f file.yaml
```

## Exam Environment

### Allowed Resources
- kubernetes.io/docs
- kubernetes.io/blog
- github.com/kubernetes
- One browser tab for exam
- One browser tab for documentation

### Not Allowed
- Personal notes
- External websites (except kubernetes.io)
- Code editors
- Multiple terminal tabs

### Terminal Tools Available
- kubectl
- kubeadm
- etcdctl
- crictl
- systemctl
- journalctl
- vim/nano
- tmux

## Exam Tips and Strategies

### Time Management
- 2 hours for 15-20 questions (~6-8 minutes per question)
- Skip difficult questions and return later
- Use bookmarking feature
- Keep track of time

### Speed Optimization
1. **Use aliases**: Set up kubectl aliases immediately
2. **Use dry-run**: Generate YAML quickly with `--dry-run=client -o yaml`
3. **Use imperative commands**: When possible, create resources imperatively
4. **Copy from docs**: Use kubernetes.io documentation for complex YAML
5. **Use explain**: `kubectl explain pod.spec.containers` for quick reference
6. **Tab completion**: Use tab to autocomplete names and paths

### Common Pitfalls
- Not reading questions carefully
- Spending too much time on one question
- Not verifying your work
- Forgetting to switch context/namespace
- Typos in commands
- Not using imperative commands when possible

### Best Practices
1. **Read carefully**: Understand what's being asked
2. **Check context**: Verify you're in the correct cluster/namespace
   ```bash
   kubectl config get-contexts
   kubectl config use-context <context-name>
   ```
3. **Verify work**: Always check that resources are created correctly
4. **Use shortcuts**: Imperative commands save time
5. **Keep notes**: Use vim to track completed questions
6. **Stay calm**: Skip and return to difficult questions

## Practice Resources

### Official Resources
- **Killer.sh**: Two free sessions included with exam registration (highly recommended)
- **kubernetes.io**: Official documentation
- **Kubernetes The Hard Way**: GitHub guide by Kelsey Hightower

### Practice Platforms
- Killer.sh (included with exam)
- KodeKloud CKA course
- A Cloud Guru CKA course
- Linux Academy
- Udemy courses (Mumshad Mannambeth)

### Lab Environments
- Minikube (local)
- Kind (Kubernetes in Docker)
- kubeadm clusters (multinode)
- Cloud providers (GKE, EKS, AKS free tier)

## Day Before Exam

### Technical Preparation
- [ ] Test your equipment (webcam, microphone)
- [ ] Test internet connection
- [ ] Clear desk area
- [ ] Have ID ready
- [ ] Review exam requirements

### Study Preparation
- [ ] Review kubectl cheat sheet
- [ ] Practice common commands
- [ ] Review troubleshooting steps
- [ ] Get good sleep

## Exam Day

### Before Exam
1. Clear your workspace
2. Close all applications except browser
3. Have ID ready
4. Start 15 minutes early
5. Complete check-in process

### During Exam
1. Set up aliases immediately
2. Read all questions first
3. Do easy questions first
4. Bookmark difficult questions
5. Verify each answer
6. Use remaining time to review

### After Each Question
- [ ] Did I read the question correctly?
- [ ] Am I in the correct context/namespace?
- [ ] Did I verify the resource was created?
- [ ] Does it meet all requirements?

## Key Topics to Master

### Must Know (Critical)
- [ ] Creating and managing pods
- [ ] Deployments and scaling
- [ ] Services and networking
- [ ] ConfigMaps and Secrets
- [ ] Troubleshooting pods and nodes
- [ ] kubectl commands
- [ ] RBAC basics
- [ ] Persistent volumes and claims

### Should Know (Important)
- [ ] StatefulSets
- [ ] DaemonSets
- [ ] Jobs and CronJobs
- [ ] Node maintenance (drain/cordon)
- [ ] etcd backup/restore
- [ ] Cluster upgrades
- [ ] Security contexts
- [ ] Network policies

### Nice to Know
- [ ] Advanced RBAC scenarios
- [ ] Custom schedulers
- [ ] Taints and tolerations
- [ ] Pod affinity/anti-affinity
- [ ] Helm basics

## Sample Exam Questions

### Question 1: Create Pod
Create a pod named nginx-pod using nginx:1.21 image in namespace web.

```bash
kubectl create namespace web
kubectl run nginx-pod --image=nginx:1.21 -n web
kubectl get pods -n web
```

### Question 2: Expose Service
Expose the nginx-pod as a NodePort service on port 80.

```bash
kubectl expose pod nginx-pod --type=NodePort --port=80 -n web
kubectl get svc -n web
```

### Question 3: Scale Deployment
Scale the nginx deployment to 5 replicas.

```bash
kubectl scale deployment nginx --replicas=5
kubectl get deployment nginx
```

### Question 4: Create ConfigMap
Create a ConfigMap named app-config with key=value: env=production

```bash
kubectl create configmap app-config --from-literal=env=production
kubectl get cm app-config -o yaml
```

### Question 5: Troubleshoot
A pod is in CrashLoopBackOff. Find the issue.

```bash
kubectl get pods
kubectl describe pod <pod-name>
kubectl logs <pod-name>
kubectl logs <pod-name> --previous
```

## Important File Locations

```bash
# Kubernetes config
/etc/kubernetes/manifests/          # Static pod manifests
/etc/kubernetes/pki/                # Certificates
/etc/kubernetes/admin.conf          # Admin kubeconfig

# kubelet config
/var/lib/kubelet/config.yaml        # kubelet configuration
/etc/systemd/system/kubelet.service # kubelet service

# etcd data
/var/lib/etcd/                      # etcd data directory

# Logs
journalctl -u kubelet               # kubelet logs
journalctl -u docker                # docker logs
/var/log/pods/                      # pod logs
```

## Quick Reference Card

### Create
```bash
k run pod --image=img
k create deploy name --image=img --replicas=3
k create svc nodeport name --tcp=80:80
k create cm name --from-literal=key=val
k create secret generic name --from-literal=pass=val
k create sa name
k create job name --image=img -- cmd
k create cronjob name --image=img --schedule="* * * * *" -- cmd
```

### Get/Describe
```bash
k get all
k get po -o wide --show-labels
k describe po name
k logs po -f --previous
k top nodes/pods
```

### Update
```bash
k edit po name
k scale deploy name --replicas=5
k set image deploy/name cont=img:tag
k rollout status/undo deploy/name
```

### RBAC
```bash
k create role name --verb=get,list --resource=pods
k create rolebinding name --role=role --serviceaccount=default:sa
k auth can-i get pods --as=user
```

### Cluster
```bash
k drain node --ignore-daemonsets --delete-emptydir-data
k uncordon node
kubeadm upgrade plan/apply
ETCDCTL_API=3 etcdctl snapshot save/restore
```

## Final Checklist

One week before:
- [ ] Complete Killer.sh practice exam
- [ ] Review all weak areas
- [ ] Practice speed optimization
- [ ] Review documentation navigation

One day before:
- [ ] Light review only
- [ ] Test equipment
- [ ] Get good rest

Exam day:
- [ ] Start early
- [ ] Clear workspace
- [ ] Stay calm
- [ ] Read carefully
- [ ] Verify answers

## Good Luck!

Remember:
- Practice, practice, practice
- Speed comes with repetition
- Read questions carefully
- Verify your work
- Stay calm and focused
- You've got this!

For more practice and detailed modules, refer to the learning modules in this application.

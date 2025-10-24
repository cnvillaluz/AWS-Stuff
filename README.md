# Kubernetes Learning Application

A comprehensive interactive learning platform for mastering Kubernetes from basics to advanced concepts and preparing for the Certified Kubernetes Administrator (CKA) certification exam.

## Features

- **Structured Learning Path**: Progress from basic to advanced Kubernetes concepts
- **Comprehensive Modules**: Detailed explanations covering all CKA exam topics
- **Hands-On Exercises**: Practice with real YAML configurations and kubectl commands
- **CKA Exam Preparation**: Complete guide with tips, strategies, and practice questions
- **Interactive Web Interface**: Easy-to-navigate platform with organized content
- **Code Examples**: Real-world examples and best practices

## Topics Covered

### Basic Concepts
- Kubernetes Architecture and Components
- Setting Up Kubernetes Environment
- Pods - The Building Blocks
- ReplicaSets and Deployments
- Services and Networking
- ConfigMaps and Secrets

### Intermediate Topics
- Storage - Volumes, PV, and PVC
- StatefulSets and DaemonSets
- Jobs and CronJobs
- RBAC and Security
- Network Policies
- Resource Management

### Advanced Topics
- Cluster Maintenance and Upgrades
- etcd Backup and Restore
- Troubleshooting and Debugging
- High Availability
- Performance Tuning

## Installation

### Prerequisites
- Python 3.8 or higher
- A Kubernetes cluster for hands-on practice (Minikube, Kind, or kubeadm)
- kubectl installed and configured

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd k8s-learning-app
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
cd web-app
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Application Structure

```
k8s-learning-app/
├── modules/
│   ├── 01-basics/          # Basic Kubernetes concepts
│   ├── 02-intermediate/    # Intermediate topics
│   └── 03-advanced/        # Advanced administration
├── exercises/
│   ├── basics/             # Basic exercises
│   ├── intermediate/       # Intermediate exercises
│   └── advanced/           # Advanced exercises
├── resources/
│   └── CKA-EXAM-GUIDE.md  # CKA exam preparation guide
├── web-app/
│   ├── app.py             # Flask application
│   ├── templates/         # HTML templates
│   └── static/            # CSS and JS files
└── requirements.txt        # Python dependencies
```

## Usage

### Learning Path

1. **Start with Basics**: Begin with Module 1 to understand Kubernetes fundamentals
2. **Progress to Intermediate**: Move to Module 2 for deeper concepts
3. **Master Advanced Topics**: Complete Module 3 for cluster administration
4. **Practice Exercises**: Work through hands-on exercises for each level
5. **CKA Preparation**: Review the exam guide when ready for certification

### Hands-On Practice

For the best learning experience:
- Set up a local Kubernetes cluster (Minikube or Kind)
- Try all kubectl commands shown in modules
- Complete the exercises in a real cluster
- Practice troubleshooting scenarios

### Setting Up Practice Environment

#### Option 1: Minikube (Recommended for beginners)
```bash
# Install Minikube
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube

# Start cluster
minikube start

# Verify
kubectl get nodes
```

#### Option 2: Kind (Kubernetes in Docker)
```bash
# Install Kind
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.20.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind

# Create cluster
kind create cluster --name learning-cluster

# Verify
kubectl get nodes
```

#### Option 3: kubeadm (Multi-node cluster)
Follow the instructions in Module 1.2: Setting Up Kubernetes Environment

## CKA Exam Preparation

This application is specifically designed to help you prepare for the CKA exam:

- **Exam-Aligned Content**: All modules map to CKA exam domains
- **Hands-On Focus**: Practice with real kubectl commands
- **Troubleshooting Skills**: Learn systematic debugging approaches
- **Time Management**: Tips for completing exam within time limit
- **Quick Reference**: Essential commands and shortcuts

Visit the CKA Exam Guide in the application for:
- Exam details and format
- Study plan (12-week schedule)
- Essential kubectl commands
- Exam tips and strategies
- Practice questions

## Contributing

This is a learning resource. If you find any issues or have suggestions for improvements:
1. Test the content thoroughly
2. Ensure all examples work
3. Follow the existing structure
4. Update documentation

## Resources

### Official Documentation
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [kubectl Cheat Sheet](https://kubernetes.io/docs/reference/kubectl/cheatsheet/)
- [CKA Exam Curriculum](https://www.cncf.io/certification/cka/)

### Practice Resources
- Killer.sh (included with CKA exam registration)
- KodeKloud CKA Course
- A Cloud Guru CKA Course

## Learning Tips

1. **Practice Daily**: Consistency is key to mastering Kubernetes
2. **Use kubectl Help**: Learn to use `kubectl explain` and `--help`
3. **Read Documentation**: Get comfortable with kubernetes.io docs
4. **Build Projects**: Create real applications on Kubernetes
5. **Join Community**: Engage with Kubernetes community forums

## Troubleshooting

### Application won't start
- Ensure Python 3.8+ is installed
- Install dependencies: `pip install -r requirements.txt`
- Check if port 5000 is available

### Can't access exercises
- Verify the exercises directory exists
- Check file permissions
- Restart the application

### Kubernetes cluster issues
- Verify cluster is running: `kubectl cluster-info`
- Check node status: `kubectl get nodes`
- Review logs: `kubectl logs -n kube-system <pod-name>`

## License

This project is created for educational purposes to help individuals learn Kubernetes and prepare for the CKA certification.

## Acknowledgments

- Kubernetes community for excellent documentation
- CNCF for the CKA certification program
- All contributors to Kubernetes education

## Contact

For questions or feedback about this learning platform, please open an issue in the repository.

---

**Start your Kubernetes journey today and become a Certified Kubernetes Administrator!**

Kubernetes Troubleshooting Task
A terminal-based engineering task that simulates real-world Kubernetes debugging scenarios. This task is designed to test problem-solving skills in container orchestration environments.

====Prerequisites
Ubuntu 22.04 LTS

Docker installed

Basic terminal knowledge
============================================================
Run the Task
bash
# Clone the repository
git clone 
cd k8s-troubleshoot-task

# Build the Docker image
docker build -t k8s-task .

# Run the solution to see it working
docker run -it k8s-task ./solution.sh

# Run the test suite
docker run -it k8s-task ./run-tests.sh
📋 Task Overview
Domain: SRE/Infra (Kubernetes Troubleshooting)

Scenario: A simple nginx web service deployment is failing with crashing pods. Your task is to diagnose and fix the Kubernetes configuration issues.

The Problem
The nginx deployment manifests have several issues causing pods to crash:

Missing container command to run in foreground

No resource limits specified

Basic Kubernetes compatibility issues

Learning Objectives
Diagnose Kubernetes pod failures

Understand container runtime requirements

Fix deployment configuration issues

Verify service accessibility

🏗️ Project Structure
text
tasks/simple-k8s-fix/
├── Dockerfile              # Environment setup with k3d & kubectl
├── task.yaml              # Task specification and requirements
├── run-tests.sh           # Test runner script
├── solution.sh            # Reference implementation
├── manifests/
│   ├── deployment.yaml    # Broken deployment (needs fixing)
│   └── service.yaml       # NodePort service definition
├── tests/
│   └── test_outputs.py    # Test suite (6 test cases)
└── requirements.txt       # Python dependencies
🧪 Test Suite
The task includes 6 comprehensive tests:

Pods Running - Verify all pods are in Running state

Pods Ready - Check containers are ready and stable

Service Accessible - Test web service on port 30080

Replica Count - Ensure correct number of replicas

No CrashLoop - Verify no pods in crashloop backoff

Deployment Healthy - Confirm successful rollout

🛠️ Technical Details
Tools Used
k3d: Lightweight Kubernetes distribution for testing

kubectl: Kubernetes command-line tool

Docker: Container runtime environment

pytest: Python testing framework

Key Kubernetes Concepts
Deployments: Manage pod replicas and updates

Services: Expose pods to network traffic

NodePort: External access to services

Resource Limits: Container resource management

Probes: Container health checking

🎯 How to Solve
Step 1: Diagnose the Issue
bash
kubectl get pods                 # Check pod status
kubectl describe pod <name>     # Get detailed pod information
kubectl logs <pod-name>         # Check container logs
Step 2: Identify Problems
Containers need to run in foreground mode

Resource limits prevent eviction

Proper port configuration required

Step 3: Apply Fixes
yaml
# Add to container spec:
command: ["nginx"]
args: ["-g", "daemon off;"]
resources:
  requests:
    memory: "64Mi"
    cpu: "50m"
  limits:
    memory: "128Mi"
    cpu: "100m"
Step 4: Verify
bash
kubectl get pods                 # Should show "Running"
curl http://localhost:30080     # Should return nginx page
kubectl rollout status deployment/nginx-deployment
📊 Validation
Baseline Test (Should Fail)
bash
docker run k8s-task bash -c "k3d cluster create test && kubectl apply -f manifests/ && sleep 20 && kubectl get pods"
# Expected: Pods in CrashLoopBackOff state
Solution Test (Should Pass)
bash
docker run k8s-task ./solution.sh
# Expected: All pods Running, service accessible
Test Suite
bash
docker run k8s-task ./run-tests.sh
# Expected: All 6 tests pass
🎓 Learning Outcomes
After completing this task, you'll understand:

Kubernetes Pod Lifecycle: How containers run in K8s

Debugging Techniques: Using kubectl for troubleshooting

Container Configuration: Making apps K8s-compatible

Service Networking: Exposing applications externally

Resource Management: Setting appropriate limits

🔧 Customization
Modify Difficulty
Add more complex issues (probes, volumes, env vars)

Introduce networking problems

Add multiple services with dependencies

Extend Testing
Add performance testing

Include security checks

Test rolling updates

🤝 Contributing
Fork the repository

Create a feature branch

Make your changes

Add tests for new functionality

Submit a pull request

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgments
Inspired by Terminal-Bench AI evaluation framework

k3d for lightweight Kubernetes testing

Kubernetes community for best practices

📞 Support
If you encounter any issues or have questions:

Check the Kubernetes Documentation

Review k3d troubleshooting guide

Open an issue on GitHub

🏆 Skills Demonstrated
Kubernetes administration

Container troubleshooting

YAML configuration

CLI proficiency

Automated testing

Problem-solving methodology

Happy Troubleshooting! 🎉



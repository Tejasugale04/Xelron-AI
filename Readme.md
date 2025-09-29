Kubernetes Troubleshooting Task
A terminal-based engineering task that simulates real-world Kubernetes debugging scenarios. This task is designed to test problem-solving skills in container orchestration environments.

====Prerequisites
Ubuntu 22.04 LTS

Docker installed

Basic terminal knowledge
============================================================
Run the Task

bash
Clone the repository
git clone https://github.com/Tejasugale04/Xelron-AI
cd Assignment_Xelron_AI

# Build the Docker image
docker build -t k8s-task .

# Run the solution to see it working
docker run -it k8s-task ./solution.sh

# Run the test suite
docker run -it k8s-task ./run-tests.sh
📋 Task Overview
Domain: SRE/Infra (Kubernetes Troubleshooting)

=================================================================================================================================================================
Scenario: A simple nginx web service deployment is failing with crashing pods. Your task is to diagnose and fix the Kubernetes configuration issues.

The Problem:
The nginx deployment manifests have several issues causing pods to crash:

Missing container command to run in foreground

No resource limits specified

Basic Kubernetes compatibility issues
================================================================================================================================================

Learning Objectives:
Diagnose Kubernetes pod failures

Understand container runtime requirements

Fix deployment configuration issues

Verify service accessibility
====================================================================================================================================

Test Suite:
The task includes 6 comprehensive tests:

Pods Running - Verify all pods are in Running state

Pods Ready - Check containers are ready and stable

Service Accessible - Test web service on port 30080

Replica Count - Ensure correct number of replicas

No CrashLoop - Verify no pods in crashloop backoff

Deployment Healthy - Confirm successful rollout

========================================================================================================

Technical Details:
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

===============================================================================================================

How to Solve:
Step 1: Diagnose the Issue
bash
kubectl get pods               
kubectl describe pod <name>     
kubectl logs <pod-name>  

========


Step 2: Identify Problems
Containers need to run in foreground mode

Resource limits prevent eviction

Proper port configuration required



======

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


===============

    
Step 4: Verify
bash
kubectl get pods                
curl http://localhost:30080    
kubectl rollout status deployment/nginx-deployment






Validation:
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







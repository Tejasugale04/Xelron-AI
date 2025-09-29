#!/bin/bash
set -euxo pipefail

echo "=== Starting K8s Troubleshooting ==="

# Start Kubernetes cluster
echo "1. Starting Kubernetes cluster..."
k3d cluster create test-cluster

# Apply broken deployment
echo "2. Applying broken deployment..."
kubectl apply -f manifests/

echo "3. Checking initial pod status..."
kubectl get pods -w &
PID=$!
sleep 15
kill $PID

# Create fixed deployment
echo "4. Creating fixed deployment..."
cat > fixed-deployment.yaml << 'EOF'
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
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
        image: nginx:1.25
        ports:
        - containerPort: 80
        command: ["nginx"]
        args: ["-g", "daemon off;"]
        resources:
          requests:
            memory: "64Mi"
            cpu: "50m"
          limits:
            memory: "128Mi"
            cpu: "100m"
EOF

echo "5. Applying fixed deployment..."
kubectl apply -f fixed-deployment.yaml

echo "6. Waiting for rollout..."
kubectl rollout status deployment/nginx-deployment --timeout=60s

echo "7. Final pod status:"
kubectl get pods

echo "8. Testing service..."
sleep 10
curl -s http://localhost:30080 | grep -o "<title>.*</title>"

echo "=== Troubleshooting Complete ==="

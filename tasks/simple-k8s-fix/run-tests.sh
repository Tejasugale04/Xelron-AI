#!/bin/bash
set -euo pipefail

echo "=== Running K8s Deployment Tests ==="

# Install test dependencies
pip3 install -r requirements.txt

# Start fresh cluster
k3d cluster delete test-cluster 2>/dev/null || true
k3d cluster create test-cluster

echo "Waiting for cluster to be ready..."
sleep 20

# Run tests
python3 -m pytest tests/test_outputs.py -v --tb=short

# Cleanup
k3d cluster delete test-cluster
echo "=== Tests Complete ==="

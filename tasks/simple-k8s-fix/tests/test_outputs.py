import pytest
import subprocess
import time
import requests

class TestK8sDeployment:
    
    def test_01_pods_running(self):
        """Test that pods are in Running state"""
        result = subprocess.run(
            ["kubectl", "get", "pods", "-l", "app=nginx", "-o", "jsonpath={.items[*].status.phase}"],
            capture_output=True,
            text=True,
            check=True
        )
        statuses = result.stdout.strip().split()
        assert all(s == "Running" for s in statuses), f"Pods not running: {statuses}"
        print("✓ All pods are Running")
    
    def test_02_pods_ready(self):
        """Test that pods are ready"""
        result = subprocess.run(
            ["kubectl", "get", "pods", "-l", "app=nginx", "-o", "jsonpath={.items[*].status.containerStatuses[0].ready}"],
            capture_output=True,
            text=True,
            check=True
        )
        ready_states = result.stdout.strip().split()
        assert all(r == "true" for r in ready_states), f"Pods not ready: {ready_states}"
        print("✓ All pods are ready")
    
    def test_03_service_accessible(self):
        """Test service accessibility"""
        time.sleep(10)  # Wait for service
        
        try:
            response = requests.get("http://localhost:30080", timeout=10)
            assert response.status_code == 200
            assert "nginx" in response.text.lower()
            print("✓ Service is accessible and returns nginx page")
        except requests.ConnectionError:
            pytest.fail("Service not accessible on port 30080")
    
    def test_04_replica_count(self):
        """Test correct number of replicas"""
        result = subprocess.run(
            ["kubectl", "get", "deployment", "nginx-deployment", "-o", "jsonpath={.status.readyReplicas}"],
            capture_output=True,
            text=True,
            check=True
        )
        assert result.stdout.strip() == "2", f"Expected 2 replicas, got {result.stdout}"
        print("✓ Correct number of replicas running")
    
    def test_05_no_crashloop(self):
        """Test no crashloop backoff"""
        result = subprocess.run(
            ["kubectl", "get", "pods", "-l", "app=nginx", "-o", "jsonpath={.items[*].status.containerStatuses[0].state.waiting.reason}"],
            capture_output=True,
            text=True
        )
        if result.stdout.strip():
            assert "CrashLoopBackOff" not in result.stdout
        print("✓ No pods in crashloop")
    
    def test_06_deployment_healthy(self):
        """Test deployment health"""
        result = subprocess.run(
            ["kubectl", "rollout", "status", "deployment/nginx-deployment", "--timeout=30s"],
            capture_output=True,
            text=True
        )
        assert result.returncode == 0
        print("✓ Deployment rollout successful")

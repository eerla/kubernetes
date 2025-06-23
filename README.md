# Docker & Kubernetes 4-Week Learning Companion

Welcome! This repository is a hands-on companion for learning Docker and Kubernetes in 4 weeks. It contains a simple Python Flask app, containerization setup, Docker Compose orchestration, and Kubernetes deployment manifests.

## 📦 What's Inside?
- **src/**: Simple Flask "Hello World" app
- **docker/**: Dockerfile, Docker Compose, and Docker installation guide
- **k8s/**: Kubernetes manifests (Deployment, Service, ConfigMap, Ingress, HPA)

---

## 🚀 Quick Start

### 1. Run Locally (No Docker)
```bash
cd src
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000

---

### 2. Docker
- See [`docker/docker-installation.md`](docker/docker-installation.md) for install instructions.
- Build & run the app:
```bash
cd docker
docker build -t flask-hello .
docker run -p 5000:5000 flask-hello
```

---

### 3. Docker Compose
- Run Flask app + Redis:
```bash
cd docker
docker-compose up
```

---

### 4. Kubernetes
- Make sure you have `kubectl` and a cluster (e.g., [minikube](https://minikube.sigs.k8s.io/)).
- Deploy everything:
```bash
kubectl apply -f k8s/
```
- Access the app via NodePort or Ingress (see `k8s/service.yaml` and `k8s/ingress.yaml`).

---

## 📚 Resources
- [Official Docker Docs](https://docs.docker.com/)
- [Official Kubernetes Docs](https://kubernetes.io/docs/)

Happy learning! 🎉 
# 🚀 GitOps Bare-Metal Home Lab: Zero to Hero

<p align="center">
  <img src="./assets/banner.png" alt="GitOps Bare-Metal Home Lab Banner" width="100%" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Kubernetes-K3s-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="K3s" />
  <img src="https://img.shields.io/badge/GitOps-Argo%20CD-EF7B4D?style=for-the-badge&logo=argo&logoColor=white" alt="Argo CD" />
  <img src="https://img.shields.io/badge/LoadBalancer-MetalLB-4B5563?style=for-the-badge&logo=icloud&logoColor=white" alt="MetalLB" />
  <img src="https://img.shields.io/badge/Ingress-Traefik-24A1C1?style=for-the-badge&logo=traefikproxy&logoColor=white" alt="Traefik" />
  <img src="https://img.shields.io/badge/Monitoring-Grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white" alt="Grafana" />
  <img src="https://img.shields.io/badge/Observability-Prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white" alt="Prometheus" />
  <img src="https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Ubuntu" />
</p>

<p align="center">
  <b>A fully reproducible bare-metal Kubernetes home lab powered by GitOps.</b><br/>
  From a fresh Ubuntu install to a self-healing cluster in minutes using one bootstrap script.
</p>

---

## 📌 Overview

Welcome to my bare-metal Kubernetes home lab.

This project transforms a normal machine such as a spare laptop, mini-PC, or home server into a **production-style cloud-native environment** using:

- **K3s** for lightweight Kubernetes
- **Argo CD** for GitOps continuous delivery
- **MetalLB** for bare-metal load balancing
- **Traefik** for ingress routing
- **Prometheus + Grafana** for observability
- **Python API + Nginx** as sample applications

The goal is simple:

> Take a **fresh Ubuntu Server installation**, run **one script**, and let the platform build itself.

This repository is designed to be both:

- a **learning project** for Kubernetes, GitOps, and observability
- a **professional portfolio project** that shows clear architecture, reproducibility, and real infrastructure thinking

---

## ✨ What This Project Demonstrates

This project showcases practical skills in:

- Kubernetes cluster bootstrapping
- GitOps workflows with Argo CD
- Bare-metal networking with MetalLB
- Ingress-based app exposure with Traefik
- Application deployment using Kubernetes manifests
- Monitoring and observability with Prometheus and Grafana
- Running reproducible infrastructure from source control

---

## 🏗️ Architecture

```mermaid
flowchart TD
    A[Fresh Ubuntu Server] --> B[Bootstrap Script]
    B --> C[Install K3s]
    B --> D[Install Argo CD]
    B --> E[Install MetalLB]

    C --> F[K3s Cluster]
    D --> F
    E --> F

    G[GitHub Repository] --> H[Argo CD Sync]
    H --> F

    F --> I[Traefik Ingress]
    F --> J[Python API]
    F --> K[Nginx App]
    F --> L[Prometheus Stack]
    F --> M[Grafana]
    F --> N[Node Exporter]

    N --> L
    L --> M

    I --> O[python.home.local]
    I --> P[grafana.home.local]
```
---
| Layer         | Tools                              |
| ------------- | ---------------------------------- |
| Kubernetes    | K3s                                |
| GitOps        | Argo CD                            |
| Ingress       | Traefik                            |
| Load Balancer | MetalLB                            |
| Monitoring    | Prometheus, Grafana, Node Exporter |
| Demo Apps     | Python API, Nginx                  |
| CI            | GitHub Actions                     |
| OS            | Ubuntu Server                      |
---
## 📂 Repository Structure

```text
.
├── .github
│   └── workflows
│       └── ci.yaml
├── apps
│   ├── nginx
│   │   ├── deployment.yaml
│   │   └── metallb-config.yaml
│   └── python-api
│       └── deployment.yaml
├── infrastructure
│   └── monitoring
│       └── prometheus-stack.yaml
├── src
│   ├── Dockerfile
│   ├── app.py
│   └── requirements.txt
└── README.md
```

## 📁 Folder Breakdown

| Path | Description |
|------|-------------|
| `.github/workflows/ci.yaml` | GitHub Actions workflow for CI checks |
| `apps/nginx/` | Kubernetes manifests for the Nginx application and MetalLB configuration |
| `apps/python-api/` | Kubernetes manifests for the Python API application |
| `infrastructure/monitoring/` | Monitoring stack manifest for Prometheus and Grafana |
| `src/` | Python application source code, dependencies, and Docker build definition |

### `src/` contents

- `app.py` — Application logic
- `requirements.txt` — Python dependencies
- `Dockerfile` — Container image build definition
## 🛠️ Prerequisites

Before getting started, make sure you have the following:

### 1. Server

A machine such as a **laptop**, **Raspberry Pi**, **mini-PC**, or **virtual machine** running a fresh installation of **Ubuntu Server**.

**Requirements:**

- Connected to your local network
- Internet access enabled
- SSH access available

### 2. Client Machine

Your everyday **Windows**, **macOS**, or **Linux** machine, used to:

- Connect to the server over SSH
- Edit the local `hosts` file
- Access dashboards and services from a web browser

## 🚀 Zero to Hero Setup

### Step 1: Fork and Prepare GitHub

Since **Argo CD** follows a **pull-based GitOps workflow**, your Kubernetes cluster must be able to read from your GitHub repository.

#### 1. Fork the Repository

Fork this repository to your own GitHub account.

#### 2. Create a GitHub Personal Access Token

Generate a **GitHub Personal Access Token (classic)** so Argo CD can authenticate against your repository.

Navigate to:

- **GitHub Settings**
- **Developer Settings**
- **Personal Access Tokens**
- **Tokens (classic)**

Create a token with the following permission:

- `repo`

Store the token somewhere safe. It should look similar to:

```text
ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
### Step 2: SSH Into Your Fresh Ubuntu Server

From your client machine, connect to the server:

```bash
ssh username@YOUR_SERVER_IP
```

Replace:

- `username` with your Ubuntu username
- `YOUR_SERVER_IP` with your server’s LAN IP address

### Step 3: Create the Bootstrap Script

Create the script file:

```bash
nano bootstrap.sh
```

Paste the following script into the file.

> **Important:** Replace every occurrence of `YOUR_GITHUB_USERNAME` with your actual GitHub username before running the script.

```bash
#!/bin/bash
set -e

echo "🚀 Bootstrapping GitOps Home Lab on a Fresh Server..."

if [ -z "$GITHUB_PAT" ]; then
  echo "⚠️ ERROR: Provide your GitHub Personal Access Token."
  echo "Run it like: GITHUB_PAT=your_github_token_here ./bootstrap.sh"
  exit 1
fi

echo "📦 1. Installing K3s Kubernetes..."
curl -sfL https://get.k3s.io | INSTALL_K3S_EXEC="--write-kubeconfig-mode 644" sh -
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
sleep 15

echo "🐙 2. Installing Argo CD & MetalLB Base..."
kubectl create namespace argocd || true
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl apply -f https://raw.githubusercontent.com/metallb/metallb/v0.14.3/config/manifests/metallb-native.yaml

echo "⏳ Waiting for Argo CD to boot (this takes a minute)..."
kubectl wait --for=condition=available deployment/argocd-server -n argocd --timeout=300s
sleep 30

echo "🔐 3. Linking Private GitHub Repo..."
cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Secret
metadata:
  name: gitops-repo-creds
  namespace: argocd
  labels:
    argocd.argoproj.io/secret-type: repository
stringData:
  url: https://github.com/YOUR_GITHUB_USERNAME/gitops-home-cluster.git
  username: YOUR_GITHUB_USERNAME
  password: $GITHUB_PAT
EOF

echo "🤖 4. Deploying GitOps Applications..."
kubectl apply -f https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/gitops-home-cluster/main/apps/nginx/deployment.yaml
kubectl apply -f https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/gitops-home-cluster/main/apps/nginx/metallb-config.yaml
kubectl apply -f https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/gitops-home-cluster/main/apps/python-api/deployment.yaml
kubectl apply -f https://raw.githubusercontent.com/YOUR_GITHUB_USERNAME/gitops-home-cluster/main/infrastructure/monitoring/prometheus-stack.yaml

echo "✅ COMPLETE! Argo CD is now taking over."
```

Save and exit:

- `Ctrl + O`, then `Enter`
- `Ctrl + X`

Make the script executable:

```bash
chmod +x bootstrap.sh
```

Run the script with your GitHub token:

```bash
GITHUB_PAT=your_github_token_here ./bootstrap.sh
```

Once started, the bootstrap process will automatically:

- Install **K3s**
- Install **Argo CD**
- Install **MetalLB**
- Connect Argo CD to your GitHub repository
- Deploy **Nginx**
- Deploy the **Python API**
- Deploy **Prometheus + Grafana**
- Apply the **MetalLB configuration**

The full setup typically completes in **3 to 5 minutes**.

## 🔁 What the Bootstrap Script Actually Does

This script is the core of the project. It performs the full cluster bootstrap from a fresh Ubuntu server and prepares the platform for GitOps-based continuous reconciliation.

### Bootstrap sequence

#### 1. Install K3s
Creates a lightweight Kubernetes cluster on your Ubuntu server.

#### 2. Install Argo CD
Deploys the GitOps controller that keeps the cluster state aligned with your repository.

#### 3. Install MetalLB
Adds `LoadBalancer` support for a bare-metal Kubernetes environment.

#### 4. Connect Argo CD to GitHub
Creates a Kubernetes secret so Argo CD can securely pull manifests from your repository.

#### 5. Deploy Platform Components
Applies the manifests for:

- **Nginx**
- **Python API**
- **Prometheus stack**
- **MetalLB configuration**

After the initial deployment, **Argo CD takes over** and continuously reconciles the live cluster state against the Git repository.

### Step 4: Configure Local DNS Resolution

Because local domains such as `python.home.local` and `grafana.home.local` are not publicly resolvable, your client machine needs a manual DNS mapping.

#### On Windows

Open **Notepad** as Administrator.

Open the following file:

```text
C:\Windows\System32\drivers\etc\hosts
```

Add these lines at the bottom:

```text
192.168.X.X    python.home.local
192.168.X.X    grafana.home.local
```

Replace `192.168.X.X` with your Ubuntu server’s actual local IP address, then save the file.

### Step 5: Access Your Cluster

Once the bootstrap process completes, you can begin accessing the deployed applications.

#### 1. Python App

Open:

```text
http://python.home.local
```

You should see the Python landing page:

```text
Hello from Python!
```
#### 2. Grafana

Open the Grafana dashboard in your browser:

```text
http://grafana.home.local
```

Log in with the default credentials:

- **Username:** `admin`
- **Password:** `admin`

After signing in, navigate to:

```text
Dashboards → Node Exporter / Nodes
```

You should see real-time infrastructure telemetry, including:

- **CPU usage**
- **Load average**
- **Memory usage**
- **System health**

#### 3. Argo CD Dashboard

To access the Argo CD web interface, port-forward the service from your Ubuntu server:

```bash
kubectl port-forward svc/argocd-server -n argocd 8080:443 --address 0.0.0.0
```

Next, retrieve the initial admin password:

```bash
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d; echo
```

Then open the following URL in your browser:

```text
https://YOUR_SERVER_IP:8080
```

Accept the browser security warning, then log in with:

- **Username:** `admin`
- **Password:** Output from the previous command

## 📸 Demo Screenshots

After adding screenshots to your repository, organize them using the following structure:

```text
assets/
├── banner.png
└── demo/
    ├── grafana-dashboard.png
    ├── python-app.png
    ├── argocd-applications.png
    ├── argocd-python-tree.png
    └── argocd-nginx-tree.png
```

### Grafana Dashboard

<p align="center">
  <img src="./assets/demo/grafana-dashboard.png" alt="Grafana Dashboard" width="100%" />
</p>

### Python App

<p align="center">
  <img src="./assets/demo/python-app.png" alt="Python App" width="100%" />
</p>

### Argo CD Applications

<p align="center">
  <img src="./assets/demo/argocd-applications.png" alt="Argo CD Applications Dashboard" width="100%" />
</p>

### Argo CD Python Resource Tree

<p align="center">
  <img src="./assets/demo/argocd-python-tree.png" alt="Argo CD Python Resource Tree" width="100%" />
</p>

### Argo CD Nginx Resource Tree

<p align="center">
  <img src="./assets/demo/argocd-nginx-tree.png" alt="Argo CD Nginx Resource Tree" width="100%" />
</p>
## 📊 Observability Stack

This repository includes a lightweight observability stack built around the core tools commonly used in real-world platform environments:

- **Prometheus** for metrics collection
- **Grafana** for dashboarding and visualization
- **Node Exporter** for host-level system metrics

Together, these components provide real-time visibility into the health and performance of your bare-metal node, making the project feel much closer to a production-style platform than a basic Kubernetes demo.

## 🐍 Python Application

The Python application lives in the `src/` directory and includes:

- `app.py`
- `requirements.txt`
- `Dockerfile`

It serves as a simple Kubernetes workload used to demonstrate:

- Container image build workflows
- Kubernetes deployment patterns
- Service exposure
- Ingress routing
- GitOps-based application delivery

## 🌍 Nginx Application

The Nginx application acts as a second sample workload inside the cluster and helps showcase:

- Kubernetes service deployment
- Application availability inside the cluster
- Exposure through **MetalLB** and **Traefik**
- Health and synchronization visibility in **Argo CD**

## 🔁 GitOps Workflow

Once the platform is up and running, the operational workflow becomes straightforward:

1. Edit manifests in Git
2. Commit the changes
3. Push to GitHub
4. Argo CD detects drift
5. Argo CD syncs the cluster
6. Kubernetes reconciles the workloads

This makes the Git repository the **single source of truth** for the entire platform.

## 🎯 Learning Outcomes

This project is a strong hands-on way to learn and demonstrate:

- Kubernetes fundamentals
- GitOps principles
- Argo CD operations
- Ingress and service exposure
- Bare-metal load balancing concepts
- Observability basics
- Infrastructure-as-code workflows
- Practical DevOps platform thinking

## 💼 Why This Is a Strong Portfolio Project

This is more than a simple toy deployment.

It demonstrates:

- Reproducible infrastructure
- Integration across multiple tools
- Real platform architecture
- Monitoring and operational visibility
- Git-based operations
- A complete end-to-end story from fresh server to running cluster

That makes it especially valuable for:

- **GitHub portfolios**
- **Internship applications**
- **DevOps engineer interviews**
- **SRE interview discussions**
- **LinkedIn technical showcases**

## 🔮 Future Improvements

Possible next steps for expanding this home lab include:

- Add TLS with **cert-manager**
- Add **Loki + Promtail** for log aggregation
- Add **Alertmanager** for alerting
- Introduce **Helm** for packaging
- Add **Kustomize** overlays
- Add **Sealed Secrets** or **SOPS**
- Expand to **multi-node K3s**
- Add **CI validation** for manifests
- Introduce **resource limits** and **autoscaling**
- Add **backup and restore** automation

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

You can contribute by:

- Improving manifests
- Expanding the monitoring stack
- Adding new workloads
- Improving CI
- Refining documentation

Please open an issue or submit a pull request.

## 📜 License

This project is licensed under the **MIT License**.

## 👨‍💻 Author

**Lakshay Walia**

If you found this project useful, consider giving it a ⭐ on GitHub.

<p align="center">
  Built with ❤️ for learning, experimentation, and real-world DevOps practice.
</p>

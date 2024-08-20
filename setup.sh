# Install webapp dependencies
pip install flask[async] pyzeebe

# Install Kubernetes & Helm
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
install minikube-linux-amd64 /usr/local/bin/minikube && rm minikube-linux-amd64
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
minikube start &

# Install the Camunda chart
helm repo add camunda https://helm.camunda.io
helm install camunda-platform camunda/camunda-platform
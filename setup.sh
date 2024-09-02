# Install webapp dependencies
pip install flask[async] pyzeebe

# Install kind
PATH=$(go env GOPATH)/bin:$PATH

# Install Kubernetes & Helm
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

# Install the Camunda chart
helm repo add camunda https://helm.camunda.io
helm install camunda-platform camunda/camunda-platform
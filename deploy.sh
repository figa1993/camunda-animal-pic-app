helm uninstall camunda-animal-pic-chart
kind delete cluster --name camunda-animal-pic-app
kind create cluster --name camunda-animal-pic-app

helm install camunda-animal-pic-chart
kubectl port-forward camunda-platform-zeebe-gateway-7ccddc7546-8962f 26500:26500 &
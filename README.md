# camunda-animal-pic-app
An example of Web App that fetches data from a Camunda client's REST API and runs locally

## Environment setup
* Install the Docker engine per the [official installation instructions](https://docs.docker.com/engine/install/)
* Install go
`sudo apt-get install golang-go`
* Install kind
`go install sigs.k8s.io/kind@v0.24.0`
* Install kubectl per the [official documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
* Install helm
`curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash`
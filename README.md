# camunda-animal-pic-app
An example of a Web Application that fetches data from a REST API whose back-end utilizes Camunda 8 to automate the process of fetching and storing of an animal image.

## Setting up the development environment
* Install the Docker Engine per the [official installation instructions](https://docs.docker.com/engine/install/)
* Install Docker Compose following the [official installation instructions](https://docs.docker.com/compose/install/)
<!-- * Install go
`sudo apt-get install golang-go`
* Install kind
`go install sigs.k8s.io/kind@v0.24.0`
* Install kubectl per the [official documentation](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)
* Install helm
`curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash` -->

## Setting up Camunda Cloud
* Create a Camunda cluster following the official documentation: https://docs.camunda.io/docs/components/console/manage-clusters/create-cluster/
* Create a new project in the Wed Modeler following the official documentation: https://docs.camunda.io/docs/components/modeler/web-modeler/launch-web-modeler/. 
* Import the ```fetch-and-store-animal-picture.bpmn``` from this repository following the official documentation: https://docs.camunda.io/docs/components/modeler/web-modeler/import-diagram/
* Deploy the process from the Web Modeler following the official documentation: https://docs.camunda.io/docs/components/modeler/web-modeler/run-or-publish-your-process/
* Create a new API client for the cluster and give it access to the Zeebe, Tasklist, and Operate scopes by following the official documentation: https://docs.camunda.io/docs/components/console/manage-clusters/manage-api-clients/. Make sure to download the Env Vars file and set the environment up with the variables and values from this file.

## Building the Docker images
### Client application
In the ```webapp``` subdirectory execute the following command:
* ```docker build -t camunda-animal-picture-client .```
### Worker application
In the ```worker``` subdirectory execute the following command:
* ```docker build -t camunda-animal-picture-worker .```


## Deploying the application
<!-- ### Postgres Database
In the ```database``` subdirectory execute the following command:
### Client Application
In the ```webapp``` subdirectory execute the following command:
* ```docker run -d -p 5000:5000 -e ZEEBE_CLIENT_ID=$ZEEBE_CLIENT_ID -e ZEEBE_CLIENT_SECRET=$ZEEBE_CLIENT_SECRET -e CAMUNDA_CLUSTER_ID=$CAMUNDA_CLUSTER_ID -e CAMUNDA_CLUSTER_REGION=$CAMUNDA_CLUSTER_REGION  camunda-animal-picture-client```
### Worker Application
In the ```worker``` subdirectory execute the following command:
* ```docker run -d -e ZEEBE_CLIENT_ID=$ZEEBE_CLIENT_ID -e ZEEBE_CLIENT_SECRET=$ZEEBE_CLIENT_SECRET -e CAMUNDA_CLUSTER_ID=$CAMUNDA_CLUSTER_ID -e CAMUNDA_CLUSTER_REGION=$CAMUNDA_CLUSTER_REGION  camunda-animal-picture-worker``` -->
* The services from which the application is composed can be deployed locally using the following command:
```docker compose up -d```
* Make sure that Camunda Cloud cluster is running
* Access the web application by opening the following URL in your system's browser: ```localhost:5000```

## @TODO
- [ ] Add ```pytest``` unit tests for the webapp and worker app to specify and test behavior for common failure modes like: being unable to reach Camunda Cloud gateway, failures when making the GET request to the APIs which return animal pictures, etc.
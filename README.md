# Tweets analysis project

This repository is a project builded by data scient students of PUC Minas. We are working on this project to exercise some skills and get some experience on data analysis. In this first version, we want create an Twitter collect tool, that can be configured for search tweets and make some basic analysis. This version has only a collector, but in future we want create:

  - A web interface to interacte with collector
  - Show one dashboard with descriptive analysis
  - Some simple real time metrics (Like the word with more frequency)

## How to run

> Before run this project, take your twitter app credentials. You will need to configure this project.

### Docker
Go to docker folder, inside this repository folder.
Get your Twitter app credentials on twitter developers page and create a .env file. This file will load your credentials on collector application. The .env file must to be like this (replace with the right values):
```
API_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
API_SECRET_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ACCESS_TOKEN_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
SEARCH="[word that you want find on tweets]"
```
Now run docker-compose up on your terminal. The first time that you run can take a fews minutes to up all services, because Docker will download and build the images. After this, you will see some logs about mongodb starting, and you will see some tweets collecteds.

### Kubernetes
Open the file collector-pod.yaml inside kubernetes folder, set the environments variables with twitter app credentials and what you want that collect find on tweets. After set this variables the file will looks like this:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: collector-pod
  labels:
    app: collector
spec:
  containers:
    - name: collector-container
      image: fernandogbi/twitter-collector:0.1
      env:
        - name: API_KEY
          value: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        - name: API_SECRET_KEY
          value: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        - name: ACCESS_TOKEN
          value: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        - name: ACCESS_TOKEN_SECRET
          value: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
        - name: SEARCH
          value: "what you want to find"
  restartPolicy: Never
```

Now, you will create mongodb and collector pods, and will create a service for mongodb. Type this commands below on your terminal:

```sh
$ kubectl create -f kubernetes/
```
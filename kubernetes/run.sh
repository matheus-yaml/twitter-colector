#!/bin/bash

source app/.env
bash env-set-kubectl.sh
kubectl apply -f colletor.yaml
kubectl apply -f counter.yaml
kubectl apply -f mongo.yaml
kubectl apply -f queue.yaml
kubectl apply -f redis.yaml
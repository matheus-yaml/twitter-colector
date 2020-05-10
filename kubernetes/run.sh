#!/bin/bash
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/vagrant/.local/bin:/home/vagrant/bin

bash env-set-kubectl.sh
kubectl apply -f colletor.yaml
kubectl apply -f counter.yaml
kubectl apply -f mongo.yaml
kubectl apply -f queue.yaml
kubectl apply -f redis.yaml
kubectl apply -f nginx.yaml
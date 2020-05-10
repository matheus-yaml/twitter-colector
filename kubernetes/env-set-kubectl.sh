#!/bin/bash
PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin:/home/vagrant/.local/bin:/home/vagrant/bin

source app/.env

B64_API_KEY=$(echo -n $API_KEY | base64 -w0)
B64_API_SECRET_KEY=$(echo -n $API_SECRET_KEY | base64 -w0)
B64_ACCESS_TOKEN=$(echo -n $ACCESS_TOKEN | base64 -w0)
B64_ACCESS_TOKEN_SECRET=$(echo -n $ACCESS_TOKEN_SECRET | base64 -w0)
B64_SEARCH=$(echo -n $SEARCH | base64 -w0)

sed "\
  s|%API_KEY|$B64_API_KEY|;\
  s|%API_SECRET_KEY|$B64_API_SECRET_KEY|;\
  s|%ACCESS_TOKEN_SECRET|$B64_ACCESS_TOKEN_SECRET|;\
  s|%ACCESS_TOKEN|$B64_ACCESS_TOKEN|;\
  s|%SEARCH|$B64_SEARCH|" \
  twitter-secrets.yaml | kubectl apply -f -




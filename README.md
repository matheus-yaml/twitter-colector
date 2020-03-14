README
======

This repository is a project for personal studies.


* How to run

Get your Twitter app credentials on twitter developers page and create a .env file. This file will load your credentials on collector application. The .env file must to be like this (replace xxx to the right values):

API_KEY=xxxxxxxxxxxxxxxxxxxxxxx
API_SECRET_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ACCESS_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
ACCESS_TOKEN_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

Now run docker-compose up on your terminal. The first time to run this can take a fews minutes, because Docker will download and build the images. After this you will see some logs about mongodb starting, and you will see some tweets collecteds.
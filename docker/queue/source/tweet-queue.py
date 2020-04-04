from redis import Redis
from flask import Flask
from flask_restful import Api, Resource
from flask import request
import requests


app = Flask(__name__)
api = Api(app, prefix = '/api/v1')

class Cache(Resource):
    def post(self):
        response = requests.post("http://counter:8080/api/v1/counter", data = {"tweet":request.form['text']})
        app.logger.info(eval(response.content))
        return 200

api.add_resource(Cache,'/cache',methods=['POST'])

app.run(host='0.0.0.0', port=5000, debug=True)
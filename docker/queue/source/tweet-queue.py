from redis import Redis
from flask import Flask
from flask_restful import Api, Resource
from flask import request
import requests


app = Flask(__name__)
api = Api(app, prefix = '/api/v1')

class Cache(Resource):
    def get(self):
        conn = Redis(host='redis',port=6379,db=0)
        results = {}
        for i in conn.keys():
            if int(conn.get(i)) > 1:
                results[i.decode(encoding="utf-8")] = int(conn.get(i))
        return results, 200


    def post(self):
        conn = Redis(host='redis',port=6379,db=0)
        response = requests.post("http://counter:8080/api/v1/counter", data = {"tweet":request.form['text']})
        words = eval(response.content)['result']
        for word in words:
            if conn.get(word) == None:
                conn.set(word,1)
            else:
                conn.set(word,int(conn.get(word))+1)
        return 200

api.add_resource(Cache,'/cache',methods=['POST','GET'])

app.run(host='0.0.0.0', port=5000, debug=True)
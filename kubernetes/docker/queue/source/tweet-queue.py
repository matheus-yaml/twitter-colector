from redis import Redis
from flask import Flask
from flask_restful import Api, Resource
from flask_cors import CORS
from flask import request
from bokeh.plotting import figure
from bokeh.embed import json_item
import requests


app = Flask(__name__)
CORS(app)
api = Api(app, prefix = '/api/v1')

class Cache(Resource):
    def get(self):
        conn = Redis(host='10.96.0.5',port=6379,db=0)
        results = {}
        for i in conn.keys():
            if int(conn.get(i)) > 1:
                results[i.decode(encoding="utf-8")] = int(conn.get(i))
        results_chart = figure(x_range=list(results.keys()))
        results_chart.vbar(x=list(results.keys()), top=list(results.values()), width=0.5)
        results_chart.xaxis.major_label_orientation = 3.14/4
        return json_item(results_chart,"chart"), 200


    def post(self):
        conn = Redis(host='redis',port=6379,db=0)
        app.logger.info(request.json)
        response = requests.post("http://10.96.0.4:8080/api/v1/counter", json = request.json)
        words = eval(response.content)['result']
        for word in words:
            if conn.get(word) == None:
                conn.set(word,1)
            else:
                conn.set(word,int(conn.get(word))+1)
        return 200

api.add_resource(Cache,'/cache',methods=['POST','GET'])

app.run(host='0.0.0.0', port=5000, debug=True)
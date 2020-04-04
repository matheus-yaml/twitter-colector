from flask import Flask
from flask_restful import Api, Resource
from flask import request

app = Flask(__name__)
api = Api(app, prefix = '/api/v1')

class WordCounter(Resource):
    def post(self):
        words = {}
        for word in request.form['tweet'].split(' '):
            if len(word) > 4 and '#' not in word and '@' not in word:
                if word not in words.keys():
                    words[word] = 1
                else:
                    words[word] += 1
        return {'result':words}, 200

api.add_resource(WordCounter,'/counter',methods=['POST'])

app.run(host='0.0.0.0', port=8080, debug=True)
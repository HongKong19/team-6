import json
from functools import lru_cache
from math import sqrt, isnan

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

import json

with open('./user_base.json') as json_file:
    data = json.load(json_file)



@app.route('/getUser')
def index():
    user = request.args.get('user')
    try:
        return json.dumps(data[user])
    except:
        return('ERROR: INVALID')



@lru_cache(maxsize=100)
def get(user):
    pass

if __name__ == '__main__':
    app.run(port=5000)

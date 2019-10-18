import json
from functools import lru_cache
from math import sqrt, isnan
import numpy as np
from flask import Flask, request
from flask_cors import CORS
from datagenerator import get_concert_list
from numpy import dot
from numpy.linalg import norm

app = Flask(__name__)
cors = CORS(app)

import json

with open('./user_base.json') as json_file:
    data = json.load(json_file)



@app.route('/getUser')
def index():
    user = request.args.get('user')
    try:
        user_data = data[user]
        return json.dumps(data[user])
    except:
        return('ERROR: INVALID')

@app.route('/CompareUser')
def compare():
    user1 = request.args.get('userA')
    user2 = request.args.get('userA')

    try:
        user1_data = data[user1]
        user2_data = data[user2]
        user1_vec = []
        user2_vec = []
        for concert in get_concert_list():
            if concert in user1_data["Concerts attended"]:
                user1_vec.append(1)
            else:
                user1_vec.append(0)
            if concert in user2_data["Concerts attended"]:
                user2_vec.append(1)
            else:
                user2_vec.append(0)
        user1_vec.append(user1_data["Revenue as client"])
        user2_vec.append(user2_data["Revenue as client"])
        user1_vec.append(user1_data["Revenue as donor"])
        user2_vec.append(user2_data["Revenue as donor"])

        user1_vec = np.array(user1_vec)
        user2_vec = np.array(user2_vec)

        cos_sim = int((dot(user1_vec, user2_vec) / (norm(user1_vec) * norm(user2_vec)))*100)
        return cos_sim

    except:
        return('ERROR: INVALID')

@lru_cache(maxsize=100)
def get(user):
    pass

if __name__ == '__main__':
    app.run(port=5000)

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


emailList = []

for user, value in data.items():
    if((int(value['RevenueAsClient'])/int(value['RevenueAsDonor'])>4)):
        emailList.append({user:value['Email']})

@app.route('/getUser')
def index():
    user = request.args.get('user')
    try:
        print(data[user])
        return json.dumps(data[user])
    except:
        return('ERROR: INVALID')

@app.route('/getEmailList')
def returnList():
    return json.dumps(emailList)

print(emailList)


@app.route('/CompareUser')
def compare():
    user1 = request.args.get('userA')
    user2 = request.args.get('userB')

    print(user1)
    print(user2)
    user1_data = data[user1]
    user2_data = data[user2]
    user1_vec = []
    user2_vec = []
    for concert in get_concert_list():
        if concert in user1_data["ConcertsAttended"]:
            user1_vec.append(1)
        else:
            user1_vec.append(0)
        if concert in user2_data["ConcertsAttended"]:
            user2_vec.append(1)
        else:
            user2_vec.append(0)
    user1_vec.append(user1_data["RevenueAsClient"])
    user2_vec.append(user2_data["RevenueAsClient"])
    user1_vec.append(user1_data["RevenueAsDonor"])
    user2_vec.append(user2_data["RevenueAsDonor"])

    user1_vec = np.array(user1_vec)
    user2_vec = np.array(user2_vec)

    cos_sim = int((dot(user1_vec, user2_vec) / (norm(user1_vec) * norm(user2_vec)))*100)
    return str(cos_sim)



@lru_cache(maxsize=100)
def get(user):
    pass

if __name__ == '__main__':
    app.run(port=5000)

import json
from functools import lru_cache
from math import sqrt, isnan

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

import json

with open('./final_user_data_team_6.json') as json_file:
    data = json.load(json_file)


emailList = []

for user, value in data.items():
    if((int(value['RevenueAsClient'])/int(value['RevenueAsDonor'])>4)):
        emailList.append({user:value['Email']})

@app.route('/getUser')
def index():
    user = request.args.get('user')
    try:
        return json.dumps(data[user])
    except:
        return('ERROR: INVALID')

@app.route('/getEmailList')
def returnList():
    return json.dumps(emailList)

print(emailList)



@lru_cache(maxsize=100)
def get(user):
    pass

if __name__ == '__main__':
    app.run(port=5000)

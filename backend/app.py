import json
from functools import lru_cache
from math import sqrt, isnan

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

g = Github(GITHUB_API_KEY)


@app.route('/')
def index():
    user = request.args.get('user')
    return json.dumps(get(user))


@lru_cache(maxsize=100)
def get(user):
    pass

if __name__ == '__main__':
    app.run(port=5000)

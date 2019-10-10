# coding=utf-8

from flask import Flask
from flask_cors import CORS
import redis
import pymongo
from bson import json_util

app = Flask(__name__)
CORS(app)

pool = redis.ConnectionPool(host='redis', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)
r.set('c', 0)

DB = pymongo.MongoClient("mongodb://mongo:27017")

db = DB["test"]

@app.route("/")
def helloWorld():
    mycol = db["customers"]
    mycol.insert_one({'name':'peng','address': 'pengliheng111@email.com'})
    data = mycol.find()
    print(data)
    return json_util.dumps({
      'message': "第"+str(r.incr('c'))+"次访问", 
      # 'data': loads(data)
    })

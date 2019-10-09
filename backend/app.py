# coding=utf-8

from flask import Flask
from flask_cors import CORS
import redis
import pymongo

app = Flask(__name__)
CORS(app)

pool = redis.ConnectionPool(host='redis', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)
r.set('c', 0)

DB = pymongo.MongoClient("mongodb://mongo:27017")

db = DB["test"]

@app.route("/")
def helloWorld():
    return "第"+str(r.incr('c'))+"次访问"

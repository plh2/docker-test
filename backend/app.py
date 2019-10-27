# coding=utf-8
import redis
import pymongo
from flask import jsonify
from flask_cors import CORS
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit, join_room, leave_room

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketIO = SocketIO(app)
CORS(app)

# redis
pool = redis.ConnectionPool(host='redis', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)
r.set('c', 0)
# db
DB = pymongo.MongoClient("mongodb://mongo:27017")
db = DB["test"]

@app.route("/")
def helloWorld():
    mycol = db["customers"]
    mycol.insert_one({'name': 'peng', 'address': 'pengliheng111@email.com'})
    data = mycol.find()
    print(data)
    return jsonify({
        'message': "第"+str(r.incr('c'))+"次访问",
        # 'data': loads(data)
    }), 200, {'Content-Type': 'application/json; charset=utf-8'}

@socketIO.on('connect')
def test_connect():
    send('User Join', broadcast=True)
    # emit({'data': 'Connected'})


# @socketIO.on('disconnect')
# def test_disconnect():
#     print('Client disconnected')


# @socketIO.on('join')
# def on_join(data):
#     print('join',data)
#     username = data['username']
#     # room = data['room']
#     # join_room(room)
#     # send(username + ' has entered the room.', room=room)


# @socketIO.on('leave')
# def on_leave(data):
#     print('leave',data)
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     send(username + ' has left the room.', room=room)


@socketIO.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    socketIO.run(app)

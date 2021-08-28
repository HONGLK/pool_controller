from asyncio.windows_events import NULL
from flask import Flask
from flask_socketio import SocketIO, disconnect
from datetime import datetime
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

class message():
    def __init__(self, Status, Message):
        self.Time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        self.Status = Status
        self.Message = Message

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)

@socketio.on('connect')
def handle_message(user):
    print(user)
    if(user == "pool_controller1"):
        print(user)
        msg = message("0000", "OK")
        print(msg, type(msg))
        # msg.Time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        socketio.emit("response", msg.toJSON())
    else:
        msg = message("0001", "User error")
        print(msg, type(msg))
        socketio.emit("response", msg.toJSON())
        #disconnect()
    

#@socketio.on('connection')
#def test_connect(auth):
#    SocketIO.send('message', {'data': 'Connected'})


if __name__ == '__main__':
    socketio.run(app)
import socketio
from datetime import datetime
import json
#import Gpio as gp
#import RPi.GPIO as GPIO

sio = socketio.Client()


class message_obj():
    def __init__(self, event, status, message):
        self.time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        self.event = event
        self.status = status
        self.message = message

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)

class controller_obj():
    def __init__(self, machineId, status):
        self.machineId = int(machineId)
        self.status = status #startUp/shutDown
        self.scheduleStart = None #datetime
        self.scheduleEnd = None #datetime
        self.time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)

class motor_obj():
    def __init__(self, status):
        self.status = status
        self.upTime = None
        self.downTime = None
        self.durations = None
        self.current = None
        self.voltage = None
        self.time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)


def gpio_controll():
    pass




@sio.on("startUp")
def handle_startUp(data):
    a = json.loads(data)
    print(a)
    #gp.relay_operation(channel)
    msg = message_obj("response", "0000", "OK")
    sio.emit("response", msg.toJSON())

@sio.on("shutDown")
def handle_shutDown(data):
    print(data)


@sio.on("response")
def handle_response(data):
    # handle the message
    print(data)

sio.connect('http://127.0.0.1:80', auth="pool_controller1")
#sio.emit('connect', "pool_controller1")
print('my sid is', sio.sid, "auth", sio.connection_auth)
sio.wait()
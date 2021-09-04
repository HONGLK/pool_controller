import socketio
from datetime import datetime
import json
import Gpio as gp
import RPi.GPIO as GPIO

from subprocess import check_output as co

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
    channel = a["machineId"]
    #gp.relay_operation(channel, 1)
    msg = message_obj("response", "0000", "OK")
    sio.emit("response", msg.toJSON())

@sio.on("shutDown")
def handle_shutDown(data):
    a = json.loads(data)
    channel = a["machineId"]
    #gp.relay_operation(channel, 0)
    msg = message_obj("response", "0000", "OK")
    sio.emit("response", msg.toJSON())

@sio.on("response")
def handle_response(data):
    msg = json.loads(data)
    if(msg["message"] == "get_IP"):
        ip = co(["curl", "ifconfig.me."]).decode("utf-8")
        return ip

sio.connect('https://pool-controller-new.herokuapp.com/', auth="pool_controller1", wait_timeout=30)
ip = co(["curl", "ifconfig.me."]).decode("utf-8")
sio.emit('Ip', ip)
print('my sid is', sio.sid, "auth", sio.connection_auth, "my IP is " + ip)
sio.wait()

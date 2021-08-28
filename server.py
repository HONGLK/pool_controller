from flask import Flask, request, abort
from flask_socketio import SocketIO, disconnect

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from datetime import datetime
import json
import os

app = Flask(__name__)
bot = LineBotApi(
    'x03RcxCzxsNWnE7tMmMB7MDNaP9WXZ0U3xgf9pJZMDTQdUdjIeH1xP2GzUvw7JFwudBENmteJoKpu+wt35fiiUt5qbs1b6eFa3qhzbw6Cdp237tZm4hVDTv4lz54rKQPzXeiCDGLToA9M+djwbZjkwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('66331e146332302e2183f569f5cb3495')

socketio = SocketIO(app)

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

@app.route("/", methods=['GET'])
def index():
    return 'TEST'


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    print("簽名:" + signature)
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
        return
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #print(event.message.text)
    #print(event.reply_token)
    #bot.reply_message(event.reply_token, TextSendMessage(event.message.text))
    if(str("啟動") in event.message.text):
        try:
            motorId = int(str(event.message.text)[-1])
            print(type(motorId), motorId)
            if(isinstance(motorId, int)):
                ctrl = controller_obj(motorId, "startUp")
                bot.reply_message(event.reply_token, TextSendMessage(str(motorId)+str("號機，啟動中...")))
                socketio.emit("startUp", ctrl.toJSON())
        except ValueError as e:
            bot.reply_message(event.reply_token, TextSendMessage(str("請在\"啟動\"後方接上控制器編號 例如:啟動1")))

@socketio.on('connect')
def handle_message(user):
    print(user)
    if(user == "pool_controller1"):
        print(user)
        msg = message_obj("response", "0000", "OK")
        print(msg, type(msg))
        # msg.Time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        socketio.emit(str(msg.event), msg.toJSON())
    else:
        msg = message_obj("response", "0001", "User error")
        print(msg, type(msg))
        socketio.emit(str(msg.event), msg.toJSON())
        #disconnect()

@socketio.on('response')
def handle_response(data):
    print(data)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    socketio.run(app, host='0.0.0.0', port=port)
    
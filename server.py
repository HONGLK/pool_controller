from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import websockets
import json
import ws_client_local as ws

app = Flask(__name__)

bot = LineBotApi(
    'x03RcxCzxsNWnE7tMmMB7MDNaP9WXZ0U3xgf9pJZMDTQdUdjIeH1xP2GzUvw7JFwudBENmteJoKpu+wt35fiiUt5qbs1b6eFa3qhzbw6Cdp237tZm4hVDTv4lz54rKQPzXeiCDGLToA9M+djwbZjkwdB04t89/1O/w1cDnyilFU=')

handler = WebhookHandler('66331e146332302e2183f569f5cb3495')


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
    if(str("啟動") == event.message.text):
        bot.reply_message(str("啟動中..."))
        trigger_local_client("startup")

def trigger_local_client(msg):
    ws.send_message




if __name__ == "__main__":
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)

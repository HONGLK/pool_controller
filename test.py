from flask import Flask, request, abort
from flask_socketio import SocketIO, disconnect

from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from datetime import datetime
import json
import os


app = Flask(__name__)

print(app)
from datetime import datetime
import RPi.GPIO as gp
import json

class message_obj():
    def __init__(self, event, status, message):
        self.time = datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S")
        self.event = event
        self.status = status
        self.message = message

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)

def relay_operation(channel, opt_status):
    relay = {
        "1" : 26,
        "2" : 20,
        "3" : 21
    }


    gp.setwarnings(False)
    gp.setmode(gp.BCM)

    gp.setup(relay["1"], gp.OUT)
    gp.setup(relay["2"], gp.OUT)
    gp.setup(relay["3"], gp.OUT)
    #0 = off, 1 = on
    try:
        if(channel in [1, 2, 3] and opt_status != gp.input(relay[str(channel)])):
            if(opt_status == 0): #opt_status = 0代表想關閉
                relay_opt = gp.LOW
                gp.ouput(relay[str(channel)], relay_opt)
                current_satus = gp.input(relay[str(channel)])

                if(current_satus == opt_status):
                    msg = message_obj("relay_operaion", "0000", "改變狀態成功，請檢查繼電器")
                    print(msg.toJSON())
                else:

                    msg = message_obj("relay_operaion", "0001", "改變狀態失敗，請檢查繼電器")
                    print(msg.toJSON())

            elif(opt_status == 1): #opt_status = 1代表想開啟
                relay_opt = gp.HIGH
                gp.ouput(relay[str(channel)], relay_opt)
                current_satus = gp.input(relay[str(channel)])
                if(current_satus == opt_status):
                    msg = message_obj("relay_operaion", "0000", "改變狀態成功，請檢查繼電器")
                    print(msg.toJSON())
                else:
                    msg = message_obj("relay_operaion", "0001", "改變狀態失敗，請檢查繼電器")
                    print(msg.toJSON())
        else:
            msg = message_obj("relay_operaion", "0002", "輸入參數錯誤，請檢查")
    except:
        msg = message_obj("relay_operaion", "1111", "Exception請檢查!")

relay_operation(1, 0)
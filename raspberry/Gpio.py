from datetime import datetime
import RPi.GPIO as gp
import json
import time
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

    gp.setup(int(relay["1"]), gp.OUT)
    gp.setup(int(relay["2"]), gp.OUT)
    gp.setup(int(relay["3"]), gp.OUT)
    print(gp.input(relay["1"]))
    print(gp.input(relay["2"]))
    print(gp.input(relay["3"]))
    print("Setup The Relay Module is [success]")

    #0 = off, 1 = on
    try:
        if(channel in [1, 2, 3] and opt_status == gp.input(relay[str(channel)])):
            if(opt_status == 0): #opt_status = 0代表想關閉 gp.HIGH為斷開
                relay_opt = gp.HIGH
                gp.ouput(relay[str(channel)], relay_opt)
                current_satus = gp.input(relay[str(channel)])

                if(current_satus == opt_status):
                    msg = message_obj("relay_operaion", "0000", "改變狀態成功，請檢查繼電器")
                    print(current_satus)
                    print(msg.toJSON())
                else:

                    msg = message_obj("relay_operaion", "0001", "改變狀態失敗，請檢查繼電器")
                    print(current_satus)
                    print(msg.toJSON())

            elif(opt_status == 1): #opt_status = 1代表想開啟 gp.LOW為導通
                relay_opt = gp.LOW
                gp.ouput(relay[str(channel)], relay_opt)
                current_satus = gp.input(relay[str(channel)])
                if(current_satus == opt_status):
                    msg = message_obj("relay_operaion", "0000", "改變狀態成功，請檢查繼電器")
                    print(current_satus)
                    print(msg.toJSON())
                else:
                    msg = message_obj("relay_operaion", "0001", "改變狀態失敗，請檢查繼電器")
                    print(current_satus)
                    print(msg.toJSON())
        else:
            msg = message_obj("relay_operaion", "0002", "輸入參數錯誤，請檢查")
    except:
        msg = message_obj("relay_operaion", "1111", "Exception請檢查!")

def test():
    Relay_Ch1 = 26
    Relay_Ch2 = 20
    Relay_Ch3 = 21

    gp.setwarnings(False)
    gp.setmode(gp.BCM)

    gp.setup(Relay_Ch1,gp.OUT)
    gp.setup(Relay_Ch2,gp.OUT)
    gp.setup(Relay_Ch3,gp.OUT)

    print("Setup The Relay Module is [success]")

    try:
            while True:
                    #Control the Channel 1
                    gp.output(Relay_Ch1,gp.LOW)
                    print("Channel 1:The Common Contact is access to the Normal Open Contact!")
                    time.sleep(0.5)

                    gp.output(Relay_Ch1,gp.HIGH)
                    print("Channel 1:The Common Contact is access to the Normal Closed Contact!\n")
                    time.sleep(0.5)

                    #Control the Channel 2
                    gp.output(Relay_Ch2,gp.LOW)
                    print("Channel 2:The Common Contact is access to the Normal Open Contact!")
                    time.sleep(0.5)

                    gp.output(Relay_Ch2,gp.HIGH)
                    print("Channel 2:The Common Contact is access to the Normal Closed Contact!\n")
                    time.sleep(0.5)

                    #Control the Channel 3
                    gp.output(Relay_Ch3,gp.LOW)
                    print("Channel 3:The Common Contact is access to the Normal Open Contact!")
                    time.sleep(0.5)

                    gp.output(Relay_Ch3,gp.HIGH)
                    print("Channel 3:The Common Contact is access to the Normal Closed Contact!\n")
                    time.sleep(0.5)

    except Exception as e:
            print(e)
            gp.cleanup()
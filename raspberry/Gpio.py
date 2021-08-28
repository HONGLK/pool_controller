from datetime import datetime
import RPi.GPIO as gp

Relay = {
    "Relay_Ch1" : 26,
    "Relay_Ch2" : 20,
    "Relay_Ch3" : 21
}

GPIO.setwarnings(Relay)
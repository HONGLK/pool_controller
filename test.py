import json
from types import ModuleType
relay = {
    "1" : 26,
    "2" : 20,
    "3" : 21
}
channel = 1
print(relay[str(channel)])
print(type(relay[str(channel)]))
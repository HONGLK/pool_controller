import json
from types import ModuleType
class message():
    def __init__(self, Status, Message):
        self.Time = 123
        self.Status = Status
        self.Message = Message
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


msg = message(123, "hi")
print(msg.toJSON())
print(type(msg))


motorId = int(4)
print(isinstance(motorId, int))
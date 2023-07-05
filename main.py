from lib import Message, DataBase, Gatherer, FrontEnd, Listener
# Aquí va la logica de fucnionamiento del condigo y la ejecucion normal del mismo

def hookDefinition(dataBase, frontEnd):
    assert isinstance(dataBase, DataBase)
    assert isinstance(frontEnd, FrontEnd)

    def hook(message):
        msg = Message(message)
        dataBase.push(msg)
        frontEnd.update(msg)

    return Listener(hook)

vcan0 = Gatherer("vcan0")
vcan1 = Gatherer("vcan1", 0x0cd)
db0 = DataBase("vcan0.csv")
db1 = DataBase("can1.csv")
front = FrontEnd()
msg1 = Message(arbitrationId=0x0c8, data=bytearray([0x1b]))
msg2 = Message(arbitrationId=0x0c8, data=bytearray([0x1a]))
hook0 = hookDefinition(db0, front)
vcan0.setHook(hook0)
hook1 = hookDefinition(db1, front)
vcan1.setHook(hook1)
vcan1.sendMessagePeriodic(0.5, msg1, msg2)
while True:
    pass

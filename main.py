from lib import Message, DataBase, Gatherer, FrontEnd, Listener
# Aquí va la logica de fucnionamiento del condigo y la ejecucion normal del mismo

# hookDefinition: DataBase FrontEnd -> Listener
# Recibe un objeto database y un objeto frontend y con estos crea el listener que retorna finalmente.
def hookDefinition(dataBase, frontEnd):
    assert isinstance(dataBase, DataBase)
    assert isinstance(frontEnd, FrontEnd)

    def hook(message):
        msg = Message(message)
        dataBase.push(msg)
        frontEnd.update(msg)

    return Listener(hook)

# requestKelly: int -> [Message]
# Recibe el id de un kelly en un entero y retorna una lista con los mensajes que se le consultaran a este kelly.
def requestKelly(kellyId):
    assert type(kellyId) == int

    return [Message(arbitrationId=kellyId, data=bytearray([0x1b])),
            Message(arbitrationId=kellyId, data=bytearray([0x1a])),
            Message(arbitrationId=kellyId, data=bytearray([0x33])),
            Message(arbitrationId=kellyId, data=bytearray([0x37])),
            Message(arbitrationId=kellyId, data=bytearray([0x42])),
            Message(arbitrationId=kellyId, data=bytearray([0x43])),
            Message(arbitrationId=kellyId, data=bytearray([0x44]))]

# Se crean los gatherers para cada canal, con sus filtros incluidos
vcan0 = Gatherer("vcan0")
vcan1 = Gatherer("vcan1", 0x0cd, 0x069)

# Se crean las databases para cada canal
db0 = DataBase("vcan0.csv")
db1 = DataBase("vcan1.csv")

# Se crea el frontend
front = FrontEnd()

# Se crean los listeners para los canales
hook0 = hookDefinition(db0, front)
hook1 = hookDefinition(db1, front)

# Se activan los listeners para cada canal
vcan0.setHook(hook0)
vcan1.setHook(hook1)

# Se crea un broadcast para hacer consultas periodicas a los componentes
vcan1.sendMessagePeriodic(0.5, *(requestKelly(0x0cd) + requestKelly(0x069)))

# Bucle general para que el codigo no se detenga.
while True:
    pass

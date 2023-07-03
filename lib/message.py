import can
from datetime import datetime

# Clase Message, la cual se hace cargo del trabajo con los mensajes can

class Message:

    # __init__: {} -> None
    # Recibe un diccionario de todos los valores. No retorna nada.
    def __init__(self, **args):
        assert type(args) == dict
        assert (("arbitrationId" in args.values()) and (type(args["arbitrationId"]) == int))
        assert (("data" in args.values()) and (type(args["data"]) == bytearray))

        if "timeStamp" in args.values():
            assert type(args["timeStamp"]) == float
            self.__timeStamp = args["timeStamp"]

        self.__arbitrationId = args["arbitrationId"]
        self.__data = args["data"]

    # getRaw: None -> (float, str)
    # No recibe nada y retorna una tupla con el primer elemento el timestamp como float y como segundo elemento la informacion del mensaje con su id.
    def getRaw(self):

        return (self.__timeStamp, str(self.__arbitrationId) + "#" + self.__data.hex())

    # getTranslate: None -> (str, [])
    # No recibe nada y retorna una tupla con el primer elemento el timestamp formateado como string y el segundo elemento el mensaje desglozado en  una lista de valores.
    def getTranslateToDatabase(self):

        translateMessage = [str(self.__arbitrationId) + "#" + self.__data.hex()]

        return (str(datetime.utcfromtimestamp(self.__timeStamp)), translateMessage)

    # getTranslate: None -> can.Message()
    # No recibe nada y retorna un objeto mensaje de la libreria can. 
    def getTranslateToLibrary(self):

        return can.Message(arbitration_id=self.__arbitrationId, data= self.__data)

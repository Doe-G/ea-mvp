import can
from datetime import datetime

# Clase Message, la cual se hace cargo del trabajo con los mensajes can

class Message:

    # __init__: can.Message() or {} -> None
    # Recibe un diccionario o un mensaje de la clase can. No retorna nada.
    def __init__(self, canMessage=None, **args):

        # Inicializa el objeto cuando ningun mensaje de la libreria can es entregado.
        if canMessage == None:
            assert type(args) == dict
            assert (("arbitrationId" in args.values()) and (type(args["arbitrationId"]) == int))
            assert (("data" in args.values()) and (type(args["data"]) == bytearray))

            if "timeStamp" in args.values():
                assert type(args["timeStamp"]) == float
                self.__timeStamp = args["timeStamp"]
            else:
                self.__timeStamp = 0.0

            self.__arbitrationId = args["arbitrationId"]
            self.__data = args["data"]

        # Inicializa el objeto cuando el mensaje de timpo can es entregado, ignorando cualquier otro paremetro entregado.
        else:
            assert isinstance(canMessage, can.Message)
            self.__timeStamp = canMessage.timestamp
            self.__arbitrationId = canMessage.arbitration_id
            self.__data = canMessage.data

    # getTranslateToDatabase: None -> (float, str)
    # No recibe nada y retorna una tupla con el primer elemento el timestamp como float y como segundo elemento la informacion del mensaje con su id.
    def getTranslateToDatabase(self):

        return (self.__timeStamp, str(self.__arbitrationId) + "#" + self.__data.hex())

    # getTranslateToFrontend: None -> (str, [])
    # No recibe nada y retorna una tupla con el primer elemento el timestamp formateado como string y el segundo elemento el mensaje desglozado en  una lista de valores.
    def getTranslateToFrontend(self):

        translateMessage = [str(self.__arbitrationId) + "#" + self.__data.hex()]

        return (str(datetime.utcfromtimestamp(self.__timeStamp)), translateMessage)

    # getTranslate: None -> can.Message()
    # No recibe nada y retorna un objeto mensaje de la libreria can. 
    def getTranslateToLibrary(self):

        return can.Message(arbitration_id=self.__arbitrationId, data= self.__data)

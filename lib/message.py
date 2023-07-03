from datetime import datetime

# Clase Message, la cual se hace cargo del trabajo con los mensajes can

class Message:

    # __init__: float, int, bytearray -> None
    # Recibe el timestamp como float, el id del mensaje como un entero y la informacion del mensaje como un bytearray. No retorna nada.
    def __init__(self, dataMessage):
        assert type(dataMessage.timeStamp) == float
        assert type(dataMessage.arbitration_id) == int
        assert type(dataMessage.data) == bytearray

        self.__message = dataMessage

    # getRaw: None -> (float, str)
    # No recibe nada y retorna una tupla con el primer elemento el timestamp como float y como segundo elemento la informacion del mensaje con su id.
    def getRaw(self):

        return (self.__timeStamp, str(self.__id) + "#" + self.__data.hex())

    # getTranslate: None -> (str, [])
    # No recibe nada y retorna una tupla con el primer elemento el timestamp formateado como string y el segundo elemento el mensaje desglozado en  una lista de valores.
    def getTranslate(self):

        translateMessage = [str(self.__id) + "#" + self.__data.hex()]

        return (str(datetime.utcfromtimestamp(self.__timeStamp)), translateMessage)

from .message import Message
# Clase DataBase: Se ocupa de trabajar el almacenamiento de los datos.

class DataBase:

    # __init__: str str str -> None
    # Recibe el nombre del archivo, el modo de escritura y el separador que tendra.
    def __init__(self, fileName, mode="a", separator=","):
        assert ((type(fileName) == str) and (fileName[-4:] == ".csv"))

        self.__stream = open(fileName, mode)
        self.__separator = ","

    # push: str [] -> None
    # Recibe una cadena de texto con el timestamp y una lista con todos los datos. Agrega los datos a la DB y no retorna nada.
    def push(self, message):
        assert isinstance(message, Message())
        timeStamp, data = message.translateToDatabase()

        self.__stream.write(timeStamp + self.__separator + self.__separator.join(data))

        return

    def pull(self, data):
        pass

    def clear(self, data):
        pass

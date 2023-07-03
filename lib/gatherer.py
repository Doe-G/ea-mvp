import can
from lib.message import Message

# Clase Gatherer, se encarga de manejar la comunicacion con la red can.

class Gatherer:

    # __init__: str, int, str -> None
    # Toma el channel como string, el bitrate como entero y la interface como string. Con esto crea un bus.
    def __init__(self, channel, bitrate, interface="socketcan"):
        assert type(channel) = str
        assert type(bitrate) = int
        assert type(interface) = str

        self.__bus=can.interface.Bus(channel=channel, interface=inteface, bitrate=bitrate)

    # getData: None -> Message()
    # No recive ningun valor y retorna el primer mensaje del bus que reciba ocupando la clase mensaje.
    def getData(self):

        data = self.__bus.recv()

        message = Message(data)

        return message

    # setHook: [func] -> None
    # Recive una lista de funciones callback y ejecuta un hook con estas. No retorna nada.
    def setHook(self, listeners):

        listeners = list(map(lambda x: can.listener(x), listeners))

        can.Notifier(self.__bus, listeners)

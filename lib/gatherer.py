import can
from .message import Message

# Clase Gatherer, se encarga de manejar la comunicacion con la red can.

class Gatherer:

    # __init__: str, int, str -> None
    # Toma el channel como string, el bitrate como entero y la interface como string. Con esto crea un bus.
    def __init__(self, channel, interface="socketcan"):
        assert type(channel) == str
        assert type(interface) == str

        self.__bus=can.interface.Bus(channel=channel, interface=interface)

    # sendData: Message() -> None
    # Recibe un numero flotante que representa el tiempo de envio y un numero no determinado de mensajes que se enviaran con la frecuencia determinada al bus.
    def sendDataPeriodic(self, period, *messages):
        assert type(period) == float

        traslatedMessages = []
        for message in messages:
            assert isinstance(message, Message)
            translatedMessages.append(message.translateToLibrary())

        can.broadcastmanager.CyclicSendTaskABC(message, period)

    # getData: None -> Message()
    # No recibe ningun valor y retorna el primer mensaje del bus que reciba ocupando la clase mensaje.
    def getData(self):

        data = self.__bus.recv()

        message = Message(timeStamp=data.timestamp, arbitrationId=data.arbitration_id, data=data.data)

        return message

    # setHook: *func -> None
    # Recibe un numero indeterminado de funciones callback y ejecuta un hook con estas. No retorna nada.
    def setHook(self, *listeners):

        #listeners = list(map(lambda x: can.Listener(x), listeners))

        can.Notifier(self.__bus, [can.Printer()])

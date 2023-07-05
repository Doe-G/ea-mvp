import can
from .message import Message

# Clase Gatherer, se encarga de manejar la comunicacion con la red can.

class Gatherer:

    # __init__: str, *int, **args -> None
    # Toma el channel como string, un numero indeterminado de ids para filtrar en la red y un numero indeterminado de parametros. Con esto crea un bus.
    def __init__(self, channel, *idsToFilter, **args):
        assert type(channel) == str

        if ("interface" in list(args.keys())):
            assert type(args["interface"]) == str
            interface = args["interface"]
        else:
            interface = "socketcan"

        filters = []
        for idToFilter in idsToFilter:
            assert type(idToFilter) == int
            filters.append({"can_id": idToFilter, "can_mask": 0xFFF})

        self.__bus=can.interface.Bus(channel=channel, interface=interface, can_filters=filters)

    # sendMessagePeriodic: Message() -> None
    # Recibe un numero flotante que representa el tiempo de envio y un numero no determinado de mensajes que se enviaran con la frecuencia determinada al bus.
    def sendMessagePeriodic(self, period, *messages):
        assert type(period) == float

        for message in messages:
            assert isinstance(message, Message)
            self.__bus.send_periodic(message.translateToLibrary(), period)


    # getData: None -> Message()
    # No recibe ningun valor y retorna el primer mensaje del bus que reciba ocupando la clase mensaje.
    def getData(self):

        data = self.__bus.recv()

        message = Message(timeStamp=data.timestamp, arbitrationId=data.arbitration_id, data=data.data)

        return message

    # setHook: *func -> None
    # Recibe un numero indeterminado de funciones callback y ejecuta un hook con estas. No retorna nada.
    def setHook(self, *listeners):
        for listener in listeners:
            assert isinstance(listener, can.Listener)

        can.Notifier(self.__bus, listeners)

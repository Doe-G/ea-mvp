import can

# Clase que se encarga de la creacion de listener para can hooks

class Listener(can.Listener):

    # __init__: func -> None
    # Recibe una funcion y crea un objeto listener con esta.
    def __init__(self, listenerFunction):
        self.__function = listenerFunction

    # on_message_received: can.Message -> None
    # Recibe un mensaje de la clase can y no retorna nada. Ejecuta con el mensaje recibido la funcion presente como atributo en la clase.
    def on_message_received(self, message):
        assert isinstance(message, can.Message)
        self.__function(message)

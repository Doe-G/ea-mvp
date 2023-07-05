import can

# Clase que se encarga de la creacion de listener para can hooks

class Listener(can.Listener):

    def __init__(self, listenerFunction):
        self.__function = listenerFunction

    def on_message_received(self, message):
        self.__function(message)

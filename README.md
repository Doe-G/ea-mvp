# eolian-mvp

Esta es una propuesta para el "Minimum Viable Product" de telemetría para el equipo eolian.

## Video prueba

Un video con una prueba realizada usando redes vcan puede encontrarse en el [siguiente link](https://youtu.be/Z1JP1W9_9Z4).

Para este video se ocupo para red vcan0 el generador "gencan" que provee la biblioteca para linux "can-utils" y para la red vcan1 se utilizo el archivo que se detalla a continuación para simular el sistema de "pregunta-respuesta" de un controlador Kelly.

```python
from typing import Any
from can import Bus, Listener, Notifier
from can.message import Message

class Kelly(Listener):
    def __init__(self, bus: Bus):
        self.bus = bus

    def on_message_received(self, msg: Message) -> None:
        if msg.arbitration_id == 0x0c8 or msg.arbitration_id == 0x064:
            req_id = msg.data[0]
            ans = Message(arbitration_id=(0x0cd if msg.arbitration_id == 0x0c8 else 0x069), data=[0xee], is_extended_id=False)
            if req_id == 0x1b:
                ans.data = [0x00, 0x01, 0x02, 0x03, 0x04]
            elif req_id == 0x1a:
                ans.data = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05]
            elif req_id == 0x33:
                ans.data = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05]
            elif req_id == 0x37:
                ans.data = [0x00, 0x01, 0x02, 0x03, 0x04]
            elif req_id == 0x42:
                ans.data = [0x00]
            elif req_id == 0x43:
                ans.data = [0x00]
            elif req_id == 0x44:
                ans.data = [0x00]
            self.bus.send(ans)


vcan1 = Bus(interface='socketcan', channel='vcan1')
notify = Notifier(vcan1, [Kelly(vcan1)])

while True:
    pass
```
Codigo de kelly.py escrito por [@Jayki-ZX](https://github.com/Jayki-ZX)

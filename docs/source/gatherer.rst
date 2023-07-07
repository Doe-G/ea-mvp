Gatherer
========

Clase que se encarga de la obtencion de datos desde los canales can.

Metodo
______

.. py:function:: eolianAPI.Gatherer(channel, *idsToFilter, **args)

   Metodo constructor de la clase, que toma el canal, los id's a filtrar en el canal y otros argumentos. Con esto setea un un canal bus con las confiuraciones definidas.

   :param channel: Obligatorio, es el nombre del canal donde se establecera el bus.
   :type  channel: str

   :param idsToFilter: Opcional, es un numero indeterminado argumentos sin un nombre como identificador, estos seran los ids que filtrara el bus a la hora de leer.
   :type idsToFilter: [int]

   :param interface: Opcional, es la interfaz por la que se va a leer el bus. Esta es parte de los argumentos que se leen por medio de **args, por lo que debe ser pasada como "interface=value" en caso de ser usada. Su valor por defecto es: "socketcan".
   :type interface: str

   :return: Este metodo retorna un objeto con todas sus configuraciones ya seteadas.
   :rtype: eolianAPI.Gatherer

.. py:function:: eolianAPI.Gatherer.sendMessagePeriodic(period, *messages)

   Esta funcion recibe un numero que representa el tiempo y un numero indefinido de mensajes y con esto comienza a enviar esta lista de mensajes con el periodo definido.

   :param period:
   :type period: float

   :param messages:
   :type messages: [eolianAPI.Messages]

   :return: El metodo no retorna nada.
   :rtype: None

.. py:function:: eolianAPI.getData()

   Este metodo no toma ningun parametro y retorna el primer mensaje que se reciba el bus.

   :return: Este metodo retorna la un objeto mensaje con la informacion extraida del bus.
   :rtype: eolianAPI.Message

.. py:function:: eolianAPI.setHook(*listeners)

   Este metodo recibe un numero indeterminado de listeners fija todos estos con un notifier, de manera que ante cada mensaje son llamados.

   :param listener:
   :type listener: [eolianAPI.Listener]

   :return: Este meotodo no retorna nada.
   :rtype: None

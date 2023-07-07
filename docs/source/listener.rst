Listener
========

Clase que se encarga de crear listeners en base a la clase abstracta de la biblioteca Python-can.

Metodos
-------

.. py:function:: eolianAPI.Listener(listenerFunction)

   Este es el metodo constructor de la clase, toma una funcion de tipo listener(recibe un can.Message y no retorna nada) y con esto crea un objeto Listener que contiene el metodo on_message_recived.

   :param listenerFunction:
   :type listenerFunction: func

   :return: Un objeto de la clase con el metodo on_message_received definido.
   :rtype: eolianAPI.Listener

.. py:function:: eolianAPI.Listener.on_message_received(message)

   Esta funcion toma un mensaje y ejecuta con este mensaje la funcion que se definio en la construccion del objeto.

   :param message:
   :type message: can.Message

   :return: El metodo no retorna nada.
   :rtype: None

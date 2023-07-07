DataBase
========

Clase que se encarga de gestionar el guardado y extraccion de datos.

Metodos
-------
.. py:function:: eolianAPI.DataBase(fileName, mode="a", separator=",")

   Metodo constructor de la clase DataBase, toma el nombre del archivo csv, el modo de escritura del archivo y el separador que se ocupara.

   :param fileName: Obligatorio, nombre del archivo en el que se trabajaran los datos. Debe de terminar en ".csv"
   :type fileName: str

   :param mode: Opcional, modo de apertura del archivo, por defecto es "a"(append). Se pueden usar todas las opciones de python para archivos: "w", "r", etc...
   :type mode: str
   
   :param separator: Opcional, el separador que se ocupara dentro dentro del archivo, por defecto es ",". Se puede ocupar cualquier separador.
   :type separator: str

   :return: Objeto tipo eolianAPI.DataBase.
   :rtype: eolianAPI.DataBase

.. py:function:: eolianAPI.DataBase.push(message)

   Metodo que agrega una nueva entrada a la database asociada al objeto.

   :param message: Obligatorio, mensaje que contiene la infromacion a publicar en la database.
   :type message: eolianAPI.Message

   :return: El metodo no retorna nada.
   :rtype: None

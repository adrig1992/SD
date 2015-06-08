#!/usr/bin/python2
# -*- coding: utf-8 -*-

"""
    Cliente.
    En base a un directorio de monitorización, estará a la espera de nuevas
    peticiones para enviar los ficheros de los que se quiere hacer una copia
    de seguridad. Existen dos opciones en el algoritmo:
        - Generación de un fichero con la lista de archivos de los que se debe
        realizar una copia de seguridad y posterior envío del mismo.
        - Envío de peticiones aisladas de ficheros. Los mismos que se deben
        encontrar dentro del archivo creado previamente.
        
"""

import zmq
import os
import subprocess

# Directorio de monitorización
DIR = 'files/bd'

def enviarFichero(fichero, sock):
    '''
    Función que envía un fichero, que es argumento de entrada.
    '''
    fn = open(fichero, 'rb')
    stream = True

    # Empieza la lectura del archivo
    while stream:
        stream = fn.read(128)
        if stream:
            sock.send(stream, zmq.SNDMORE)
        else:
            sock.send(stream)

    print "Archivo " + fichero + " enviado"


def server():
    '''
    Servidor. En este caso actúa como cliente. Espera la petición del servidor
    y envía el archivo correspondiente.
    '''

    context = zmq.Context(1)
    sock = context.socket(zmq.REP)
    sock.bind('tcp://*:4545')

    print "Servidor cliente en ejecucion"
    # Bucle principal
    while True:
        # Obtenemos el mensaje
        msg = sock.recv()
        # Concatenamos el directorio que se est
        if msg == 'copy':            
            # Comprobamos que el fichero existe
            if not os.path.isfile(DIR):
                sock.send('')
                print "El archivo " + DIR + " no se encuentra en el sistema"
                continue
            enviarFichero(DIR, sock)
        else:
		    print "Opción incorrecta"

if __name__ == '__main__':
    server()

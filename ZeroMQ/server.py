#!/usr/bin/python2
# -*- coding: utf-8 -*-
"""
    Realizará una petición cada TIME tiempo a los nodos que estén en la red,
    de manera que cada uno de ellos subirá los ficheros nuevos o modificados.
"""

import zmq
import os
import time
import sys
import subprocess

rango = [9, 12]

def main():
    while True:
        time.sleep(5)
        print "Nuevo evento"
        for ping in rango:
            time.sleep(2)
            address = "127.0.0" + str(ping)
            res = subprocess.call(['ping', '-c', '1', '-W', '1', address], stdout=open(os.devnull, "wb"), stderr=open(os.devnull, "wb"))
            if res == 0:
                print "Ping correcto. ", address
                context = zmq.Context()
                socket = context.socket(zmq.REQ)
                socket.connect('tcp://'+address+':4545')
                dest = open(os.path.basename('files/bd'), 'w+')
                socket.send('copy')

                while True:
                    # Start grabing data
                    data = socket.recv()
                    # print data
                    # Write the chunk to the file
                    dest.write(data)
                    if not socket.getsockopt(zmq.RCVMORE):
                        # If there is not more data to send, then break
                        break
	
                dest.close()
                print "Copia de seguridad realizada"
                time.sleep(0.5)
                os.chdir('..')


if __name__ == '__main__':
    #get_file(sys.argv[1])
    main()

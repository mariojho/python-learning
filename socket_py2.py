#!/usr/bin/env python
import socket
print ('creacion del socket')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Socket creado')
print ("Conexión al host remoto")
s.connect(('www.ediciones-eni.com', 80))
print('Conexión efectuada')
s.send(b'GET /index.html HTML/1.1\r\n\r\n')
while 1:
    data = s.recv(128)
    print(data)
    if data == "":
        break
s.close

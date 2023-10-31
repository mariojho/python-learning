#!/usr/bin/env python
import socket
print ('creacion de socket...')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('socket creado')
print("conexion al host remoto")
s.connect(('www.ediciones-eni.com', 80))
print('conexion efectuada')
s.send(b'GET /index.html HTML/1.1\r\n\r\n')
data = s.recv(2048)
print(data)
s.close()
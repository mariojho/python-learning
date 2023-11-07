#!/usr/bin/env python
# coding=utf-8

import socket, sys
from OpenSSL import SSL

ctx = SSL.Context(SSL.SSLv23_METHOD)
print(u"Creación del socket...")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket creado")

ssl = SSL.Connection(ctx, s)
print("Establecimiento de SSL...")
ssl.connect(('www.openssl.org', 443))
print(u"Conexión efectuada")
print("Consulta solicitada")
ssl.sendall(b"GET / HTTP/1.0\r\n\r\n")
print("Consulta efectuada")

while 1:
    try:
        buf = ssl.recv(2048)
    except SSL.ZeroReturnError:
        break
    print(buf)
ssl.close()
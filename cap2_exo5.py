#!/usr/bin/env python
#--*-- coding:UTF-8 --*--
import socket, sys
host = sys.argv[1]
textport = sys.argv[2]
archivo = sys.argv[3]

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as e:
    print ("Error en la creación del socket: %s" %e)
    sys.exit(1)

try:
    port = int(textport)
except ValueError:
    try:
        port = socket.getservbyname(host, 'tcp')
    except socket.error as e:
        print ("No se encuentra el puerto %s" %e)
        sys.exit(1)

try:
    s.connect((host, port))
except socket.gaierror as e:
    print ("Error de dirección de conexión al servidor: %s" %e)
    sys.exit(1)
except socket.error as e:
    print("error de conexion %s" %e)
    sys.error(1)
data = ""

try:
    s.sendall(b'GET %s HTTP/1.0\r\n\r\n' %archivo.encode() )
except socket.error as e:
    print ("Error de envío de datos: %s " %e)
    sys.exit(1)
while 1:
    try:
        buf = s.recv(2048)
    except socket.error as e:
        print ("Error de recepción de datos %s " %e)
        sys.exit(1)
    if not len(buf):
        break
    print (buf)

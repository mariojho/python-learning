# Cliente que se conecta a un servidor y recibe un mensaje desde cap2_exo7.py servidor
#!/usr/bin/env python
import socket, time

host = socket.gethostbyname(socket.gethostname())
print (host)
port = 1234 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

client, direccion = s.accept()
print (direccion)
print ("Se ha efectuado una conexión desde")
print (client.getpeername())
client.close()
s.close()

# Conversación con el cliente
#!/usr/bin/env python
# --*-- coding: utf-8 --*--
import socket 
host=''
port = 1338
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
cliente, direccion = s.accept()
print(direccion)
print (cliente.getpeername())
cliente.send(b"Hola ediciones ENI introduzca una palabra o fin si desea terminar la conversacion\r\n")

while 1:
    data = cliente.recv(1024)
    if data == "fin\n":
        break
    print ("Cliente > " + data.decode()) 
    palabra = input("Servidor >") # user input insead raw_input for 3.x python version
    cliente.send(palabra.encode())

cliente.close()
s.close()
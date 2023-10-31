
import socket
print ('creacion de socket')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('socket efectuado')
print ('conexion al host remoto')
print(s)
s.connect(('www.ediciones-eni.com', 80))
print ('conexion efectuada')


# Servidor TCP que escucha en el puerto 1234, cap2_exo8.py - para el cliente
import socket

host = ''
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SOREUSEADDR, 1)
s.bind((host, port))
s.listen(5)


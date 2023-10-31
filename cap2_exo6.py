#!/usr/bin/env python
#--*-- coding:UTF-8 --*--
import socket 
host = "ftp.ibiblio.org"
port = 21 
def fin():
    data = s.recv(1024)
    print (data)
    if data == "":
        pass

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
fin()

s.send(b"USER anonymous\r\n")
fin()

s.send(b"PASS pepe@casa.es\r\n")
fin()

s.send(b"HELP \r\n")
fin()

s.send(b"QUIT \r\n")
s.close()
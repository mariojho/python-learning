#!/usr/bin/env python 
import sys, smtplib 

fromaddr = input("From: ")
toaddrs = str.split(input("To: "), ',')
print("Introduzca el mensaje: ")
msg = ''

while 1:
    line = sys.stdin.readline()
    if not line:
        break 
    msg = msg + line 

server = smtplib.SMTP('localhost')
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
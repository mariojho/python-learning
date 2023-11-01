#!/usr/bin/env python
import sys, socket
result = socket.getaddrinfo(sys.argv[1],None)
contador = 0
for item in result:
    print ("%-2d: %s" % (contador,item[4]))
    contador += 1
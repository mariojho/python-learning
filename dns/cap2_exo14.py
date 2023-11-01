#!/usr/bin/env python
# --*-- coding: utf-8 --*--
import sys, socket 
try:
    result = socket.gethostbyaddr("8.8.8.8")
    print("El nombre del host primario es:")
    print (" "+ result[0])
    print("\nDirección:")
    for item in range(2):
        print(" " + item.__str__())
except socket.herror as e:
    print("No se ha podido resolver", e)
# Ejercicio Web 
# Actualizado la versión del libro de Python 2.7 a Python 3.6
# http://www.python.org/doc/current/lib/module-urllib.html
#!/usr/bin/env python 
# --*-- coding: utf-8 --*--
import sys
import urllib.request as ur
req = ur.Request(sys.argv[1])
fd = ur.urlopen(req)

while 1:
    data = fd.read(1024)
    if not len(data):
        break
    print(data)
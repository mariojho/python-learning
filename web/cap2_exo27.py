# Ejercicio Web - Método POST
# Actualizado la versión del libro de Python 2.7 a Python 3.6
# http://www.python.org/doc/current/lib/module-urllib.html

#!/usr/bin/env python 
# --*-- coding: utf-8 --*--

import sys, urllib.request as urllib_request
import urllib.parse as urllib_parse

consulta = sys.argv[1]
url = 'https://es.search.yahoo.com/search'
data = urllib_parse.urlencode([('p', consulta)])
req = urllib_request.Request(url)
fd = urllib_request.urlopen(req, data.encode())
file = open("Resultado.html", "w")

while 1:
    data = fd.read(1024)
    if not len(data):
        file.close()
        break
    file.write(data.decode())
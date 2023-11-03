# Ejercicio Web - Método Get
# Actualizado la versión del libro de Python 2.7 a Python 3.6
# http://www.python.org/doc/current/lib/module-urllib.html

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.parse as ur

def addGETdata(url, data):
    return url + '?' + ur.urlencode(data)

site = input("Indique la url \n")
query = input('Indique la variable\n')
dato = input('Indique el dato \n')
url = addGETdata(site, [(query, dato)])
print("Utilizamos la url ", url)
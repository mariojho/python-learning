# Analizar páginas HTML y XHTML. Recuperar enlaces de una página HTML.
# Modificado original del libro
# Actualizado la versión del libro de Python 2.7 a Python 3.6

#!/usr/bin/env python
import urllib.request as urllib_request
from bs4 import BeautifulSoup

linweb = urllib_request.urlopen("https://www.python.org/")
pageweb = linweb.read()
sopa = BeautifulSoup(pageweb, "lxml")
print(u"\n\n Visualizar todos los enlaces de la página.")
print (sopa('a'))
print (u"\n\n Visualizar el primer enlace de la página")
print (sopa('a')[0])
print(u"\n\n Visualizar el atributo href del primer enlace encontrado")
print (sopa('a')[0]["href"])
print(u"\n\n Visualizar el atributo href de todos los enlaces encontrados")

for i in sopa('a'):
    try:
        print(i["href"])
    except:
        pass

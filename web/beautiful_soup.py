# Analizar páginas HTML y XHTML. Recuperar datos de una página HTML. cap2_HTML3.html
# Modificado original del libro
# Actualizado la versión del libro de Python 2.7 a Python 3.6

#!/usr/bin/env python

import urllib.request as urllib_request 
from bs4 import BeautifulSoup

vincweb = urllib_request.urlopen("https://www.python.org/")
pageweb = vincweb.read()
soup = BeautifulSoup(pageweb, "lxml")
print("Visualizar la etiqueta TITLE")
print(soup.html.head.title)
print("Visualizar sólo el título")
print(soup.html.head.title.string)
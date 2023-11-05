#!/usr/bin/env python

import urllib.request as urllib_request
from bs4 import BeautifulSoup
import re  

enlaceweb = urllib_request.urlopen("https://www.python.org/")
paginaweb = enlaceweb.read()
sopa = BeautifulSoup(paginaweb, "lxml")
print(u"Contamos el número de etiquetas td")
print(len(sopa('td')))
print("Ahora contamos las etiquetas td de clase body")
print(len(sopa('td', {"class":"body"})))

# Usando expresiones regulares
print("Contando con expresiones regulares")
print(sopa('td',{"class":re.compile('^.*r$')}))
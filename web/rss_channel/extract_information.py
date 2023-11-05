# Extracción de contenido de un canal RSS.
# Modificado original del libro
# Actualizado la versión del libro de Python 2.7 a Python 3.6

#!/usr/bin/env python

import urllib.request as urllib_request
from xml.dom import minidom

def getTextFromNode(node):
    """extraer el texto de una etiqueta (nodo)"""
    return "".join([n.nodeValue for n in node.childNodes if n.nodeType == n.TEXT_NODE])

doc = minidom.parse(urllib_request.urlopen("https://feeds.megaphone.fm/newheights"))

print("<h1>RSS news</h1>")
print("<ol>")

for item in doc.getElementsByTagName("item")[:3]:
    print('<li>\n <a href="%s">%s</a>\n</li>' %(getTextFromNode(item.getElementsByTagName("link")[0]), getTextFromNode(item.getElementsByTagName("title")[0])))

print("</ol>")
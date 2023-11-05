# Analizar páginas HTML y XHTML. Para crear documentos XML
# Modificado original del libro
# Actualizado la versión del libro de Python 2.7 a Python 3.6
# Para ejecutar el ejercicio hacen falta dos ficheros de imagen

#!/usr/bin/env python 
# --*-- coding: UTF-8 --*--

from xml.dom.minidom import Document
from xml.dom import minidom, xmlbuilder

doc = Document()
nodo_root = doc.createElement("inicio")
doc.appendChild(nodo_root)

como = doc.createComment("Esto es un ejemplo")
nodo_root.appendChild(como)

titulo = doc.createElement("nombre")
nodo_root.appendChild(titulo)

contenido = doc.createElement("Programación Python")
titulo.appendChild(contenido)

element = doc.createElement("Capítulo")
element.setAttribute("Número", "1")

nodo_root.appendChild(element)

titulo = doc.createElement("nombre")
element.appendChild(titulo)

contenido = doc.createTextNode("Introducción")

titulo.appendChild(contenido)
fecha = doc.createElement("fecha")
fecha.setAttribute("dia", "14")
fecha.setAttribute("mes", "Enero")
fecha.setAttribute("año", "2012")
element.appendChild(fecha)

img = doc.createElement("img")
img.setAttribute("src", "logo1.png")
element.appendChild(img)

autor = doc.createElement("autor")
element.appendChild(autor)

contenido = doc.createTextNode("Ebel Franck")
autor.appendChild(contenido)

element = doc.createElement("Capítulo")
element.setAttribute("Número", "2")
nodo_root.appendChild(element)

titulo = doc.createElement("nombre")
element.appendChild(titulo)

contenido = doc.createTextNode("Introducción")
titulo.appendChild(contenido)

fecha = doc.createElement("fecha")
fecha.setAttribute("dia", "15")
fecha.setAttribute("mes", "Enero")
fecha.setAttribute("año", "2012")
element.appendChild(fecha)

img = doc.createElement("img")
img.setAttribute("src", "logo2.png")
element.appendChild(img)

autor = doc.createElement("autor")
element.appendChild(autor)

contenido = doc.createTextNode("Ediciones ENI")
autor.appendChild(contenido)

def output_xml(doc, dir_xml):
    file = open(dir_xml, "w")
    file.write(doc.toprettyxml())

output_xml(doc, "mi_primer_documento.xml")
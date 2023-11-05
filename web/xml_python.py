#!/usr/bin/env python 
#Coding: UTF-8

from xml.dom.minidom import Document

document = Document() 
raiz = document.createElement("raiz")
document.appendChild(raiz)
child = document.createElement("child")
child.setAttribute("id", "10")
raiz.appendChild(child)
print(document.toxml())
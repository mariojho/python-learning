# Analizar páginas HTML y XHTML. Recuperar datos de una página HTML.
# Modificado original del libro
# Actualizado la versión del libro de Python 2.7 a Python 3.6
#!/usr/bin/env python

from html.parser import HTMLParser
import sys 

class TitleParser(HTMLParser):
    def __init__(self):
        self.title = ""
        self.readingtitle = 0
        HTMLParser.__init__(self)

    def handle_starting(self, tag, attrs):
        if tag == 'title':
            self.readingtitle = 1 

    def handle_data(self, data):
        if self.readingtitle:
            self.title += data 
    
    def handle_endtag(self, tag):
        if tag == "title":
            self.readingtitle = 0 

    def gettitle(self):
        return self.title 
    
fd = open(sys.argv[1])
tp = TitleParser()
tp.feed(fd.read())
# Obtener los datos de cap2_HTML.html
print("El título es: ", tp.gettitle())

# Analizar páginas HTML y XHTML. Recuperar datos de una página HTML. cap2_HTML3.html
# Modificado original del libro
# Actualizado la versión del libro de Python 2.7 a Python 3.6
#!/usr/bin/env python

from html.entities import entitydefs
from html.parser import HTMLParser
import sys

class TitleParser(HTMLParser):

    def __init__(self):
        self.title = ""
        self.readingtitle = 0
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrrs):
        if tag == 'title':
            self.readingtitle = 1

    def handle_data(self, data):
        if self.readingtitle:
            self.title += data

    def handle_endtag(self, tag):
        if tag == "title":
            self.readingtitle = 0

    def handle_entityref(self, name):
        if entitydefs.has_key(name):
            self.handle_data(entitydefs[name])
        else:
            self.handle_data('&' + name + ';')

    def handle_charref(self, name):
        try:
            charnum = int(name)
        except ValueError:
            return 
        if charnum < 1 or charnum > 255:
            return 
        self.handle_data(chr(charnum))

    def gettitle(self):
        return self.title 
    
fd = open(sys.argv[1])
tp = TitleParser()
tp.feed(fd.read()) 
print ("El título es: ", tp.gettitle())           

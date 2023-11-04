# Actualizado la versión del libro de Python 2.7 a Python 3.6
#!/usr/bin/env python 
# --*-- coding: utf-8 --*--

from html.parser import HTMLParser 
import sys 

class TitleParser(HTMLParser):
    
    def __init__(self):
        self.body = ""
        self.readingbody = 0
        HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'body':
            self.readingbody = 1

    def handle_data(self, data):
        if self.readingbody:
            self.body += data 

    def handle_endtag(self, tag):
        if tag == "body":
            self.readingbody = 0

    def getbody(self):
        return self.body 
    
fd = open(sys.argv[1])
tp = TitleParser()
tp.feed(fd.read())
print ("El BODY es: ", tp.getbody())
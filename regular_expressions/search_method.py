# Expresiones regulares 

import re 
cadena = "Edición ENI"
re.search('ENI', cadena)
if re.search('ENI', cadena):
    print(u"La expresión regular funciona")
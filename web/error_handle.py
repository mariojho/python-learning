# Manejo de errores en la conexión a un servidor web
# Actualizado la versión del libro de Python 2.7 a Python 3.6
# http://www.python.org/doc/current/lib/module-urllib.html

import urllib.request as urllib_request
import sys

try:
    fd = urllib_request.urlopen("https://www.google.com/chuchita")
except urllib_request.URLError as e:
    print("Error de conexión: ", e)
    print(e.reason)
    sys.exit(1)
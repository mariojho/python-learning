# Ejercicio conexión Web: Autenticación
# Actualizado la versión del libro de Python 2.7 a Python 3.6
# http://www.python.org/doc/current/lib/module-urllib.html

#!/usr/bin/env python

import sys, urllib.request as urllib_request, getpass 

class TerminalPassword(urllib_request.HTTPPasswordMgr):
    def find_user_password(self, realm, authuri):
        retval = urllib_request.HTTPPasswordMgr.find_user_password(self, realm, authuri)
        if retval[0] == None and retval[1] == None:
            sys.stdout.write("Se requiere un login para %s en %s\n" %(realm, authuri))
            username = sys.stdin.readline().rstrip()
            password = getpass.getpass().rstrip()
            return(username, password)
        else:
            return retval
        
req = urllib_request.Request(sys.argv[1])
opener = urllib_request.build_opener(urllib_request.HTTPBasicAuthHandler(TerminalPassword()))
fd = opener.open(req)
print("Intento ", fd.geturl())
info = fd.info()
for key, value in info.items():
    print ("%s = %s" %(key, value))
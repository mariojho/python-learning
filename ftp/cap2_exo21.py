# Envío de datos
#!/usr/bin/env python
#--*-- coding: utf-8 --*--
from ftplib import FTP 
import sys, getpass, os.path 
host, username, localfile, remotepath = sys.argv[1:]
password = getpass.getpass("Introduzca la contraseña para %s en %s" %(username, host))
f = FTP(host)
f.login(username, password)
f.cwd(remotepath)
fd = open(localfile, 'rb')
f.storbinary('STOR %s' %os.path.basename(localfile),fd)
fd.close()
f.quit()

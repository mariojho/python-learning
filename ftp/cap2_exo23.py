# FTP: listar el contenido de las carpetas
# Ejemplo con dir()
#!/user/bin/env python
#--*-- coding: utf-8 --*--
from ftplib import FTP 
f = FTP('ftp.obspm.fr')
f.login()
f.cwd('/')
entrada = []
f.dir(entrada.append)
print("%d entradas: " %len(entrada))
for item in entrada:
    print(item)
f.quit()
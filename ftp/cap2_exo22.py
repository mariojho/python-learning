#!//usr/bin/env python
#--*-- coding: utf-8 --*--
from ftplib import FTP 
f = FTP('ftp.obspm.fr')
f.login() 
f.cwd('/')
entrada = f.nlst()
entrada.sort()
print ("%d entradas: "%len(entrada))
for item in entrada:
    print(item)
f.quit()
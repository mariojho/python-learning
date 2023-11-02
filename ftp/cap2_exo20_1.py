#!/usr/bin/env python
#--*-- coding: utf-8 --*--
from ftplib import FTP 
import sys
f = FTP('ftp.obspm.fr')
f.login()
f.cwd('/v1.0')
f.voidcms("TYPE I")
datasock, estsize = f.ntransfercmd("RETR linux-1.0.tar.gz")
transbytes = 0
fd = open('linux-1.0.tar.gz', 'wb')

while 1:
    buf = datasock.recv(2048)
    if not len(buf):
        break
    fd.write(buf)
    transbytes += len(buf)
    print("Recepción de %d" %transbytes)
    if estsize:
        print("en %d bites (%.1f%%)\r"%(estsize, 1000.0 * float(transbytes)/float(estsize)))
    else:
        print("bytes\n")
    print("\n")

fd.close()
datasock.close()
f.voidresp()
f.quit()


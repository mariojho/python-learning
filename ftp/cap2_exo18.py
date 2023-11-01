#!/usr/bin/env python
# --*-- coding: utf-8 --*--
from ftplib import FTP
f = FTP('ftp.obspm.fr')
print("Hola: ", f.getwelcome())
f.login()
print("CWD:", f.pwd())
f.quit()
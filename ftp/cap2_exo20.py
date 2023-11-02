#!/usr/bin/env python
#--*-- coding: utf-8 --*--
from ftplib import FTP 
f = FTP('ftp.obspm.fr')
f.login()
f.cwd('/')
fd = open('patch8.gz', 'wb')
f.retrbinary('RETR patch8.gz', fd.write)
fd.close()
f.quit()


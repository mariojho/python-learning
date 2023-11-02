#!/usr/bin/env python
#--*-- coding: utf-8 --*--
from ftplib import FTP

def writeline(data):
    fd.write(data+'\n')

f = FTP('ftp.obspm.fr')
f.login()
f.cwd('/')
fd = open('README', 'w')
f.retrlines('RETR README', writeline)
fd.close()
f.quit()
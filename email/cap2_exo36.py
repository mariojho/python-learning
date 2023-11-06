#!/usr/bin/env python
import sys, email, time 
from email import utils 

def getdate(msg):
    if not 'date' in msg:
        return None 
    datehdr = msg['date'].strip()
    try:
        return utils.mktime_tz(utils.parsedate_tz(datehdr))
    except:
        return None 

msg = email.message_from_file(sys.stdin)
dateval = getdate(msg)
    
if dateval is None:
    print("No se ha encontrado una fecha válida")
else:
    print("El mensaje ha sido enviado el: ", time.strftime('%A, %B %d %Y %I:%M %p', time.localtime(dateval)))

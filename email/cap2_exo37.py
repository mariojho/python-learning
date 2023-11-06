#!/usr/bin/env python 
import sys, smtplib, socket 

if len(sys.argv[1]) < 4:
    print("La sintaxis es la siguiente: %s servidor_direccion_fuente direccion_destino [direccion_destino...]" %sys.argv[0])
    sys.exit(255)

server = sys.argv[1]
fromaddr = sys.argv[2]
toaddrs = sys.argv[3]

message = """to: %s
From: %s
Subject: Test de mensaje 

saludo,

He aquí un mensaje enviado mediante smtplib.
"""%(','.join(toaddrs), fromaddr)

try:
    s = smtplib.SMTP(server)
    s.set_debuglevel(1)
    s.sendmail(fromaddr, toaddrs, message)
except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException) as e:
    print("*** Su mensaje no ha podido ser enviado ***")
    print(e)
    sys.exit(1)
else:
    print(u"Su mensaje ha sido enviado con éxito a %d destinatario(s)"%len(toaddrs))
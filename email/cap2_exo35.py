# Se tiene que introducir el archivo email.txt: 
# $cap2_exo35.py < email.txt
#!/usr/bin/env python

import sys, email 

msg = email.message_from_file(sys.stdin)
print("*** Cabeceras del mensaje: ")
for header, value in msg.items():
    print(header + ":")
    print(" " + value)

if msg.is_multipart():
    print("Este programa no soporta los correos multipart")
    sys.exit(1)

print("-" * 78)
if 'subject' in msg:
    print("Asunto: ", msg['subject'])
    print("-" * 78)

print("Cuerpo del mensaje:")
print("")
print(msg.get_payload())

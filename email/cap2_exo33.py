#!/usr/bin/env python

import smtplib 
from email.mime.text import MIMEText
from email import utils

de = input("De: ")
para = input("Para: ")
asunto = input("Asunto: ")
fecha = input("Introduzca la fecha: ")
print("Introduzca su mensaje: \n")
msg = ''
while 1:
    line = input()
    if not len(line):
        break 
    msg = msg + line 

mail = MIMEText(msg)
mail['From'] = de 
mail['Subject'] = asunto
mail['To'] = para 
mail['Date'] = fecha
mail['Message-ID'] = utils.make_msgid()

server = smtplib.SMTP('smtp.gmail.com', 587)
print("Configuración del servidor SMTP")
server.sendmail(de, [para], mail.as_string())
print("El mensaje se ha enviado")
server.quit()
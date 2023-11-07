#!/usr/bin/env python
#coding=utf-8
from email.mime.text import MIMEText
from email import message_from_string
from email.message import Message
import poplib

servidor_pop = poplib.POP3("pop.domain.com")
servidor_pop.user("javier")
servidor_pop.pass_("python")
nb, tam = servidor_pop.stat()
print("Número de mails = ", nb)
print("\n Tamaño total = ", tam)

for i in range(nb):
    print("---------------------")
    print("Mensaje urgente")
    print("---------------------")
    message = servidor_pop.ret(i + 1)
    mail_inline = ""
    for linea in message[1]:
        mail_inline = mail_inline + "\n"
        mi_obj_message = message_from_string(mail_inline)
        print(mi_obj_message.get_payload('From'))
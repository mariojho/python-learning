#!/usr/bin/env python

import poplib
servidor_pop = poplib.POP3("pop.domain.com")
servidor_pop.user("javier")
servidor_pop.pass_("python")
nb, tam = servidor_pop.stat()
print("Número de mails = ", nb)
print("\n Tamaño total = ", tam)

for i in range(nb):
    message = servidor_pop.ret(i + 1)
    print(message[0])
    for linea in message[1]:
        print(linea)
    print(message[2])
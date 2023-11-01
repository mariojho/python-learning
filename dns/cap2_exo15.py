#!/usr/bin/env python
# --*-- coding: utf-8 --*--
# Requiere DNS la versión 2.4 de Python para ejecutar este script
import sys,DNS
query = sys.argv[1]
DNS.DiscoverNameServers()
reqobj = DNS.Request()
answerobj = reqobj.req(name=query, qtype=DNS.Type.ANY)
if not len(answerobj.answers):
    print("No encontrado")
for item in answerobj.answers:
    print("%-5s %s" % (item['typename'],item['data']))
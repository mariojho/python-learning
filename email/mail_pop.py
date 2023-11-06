#!/usr/bin/env python

import poplib 

servidor_pop = poplib.POP3("pop.domain.com")
servidor_pop.user("javier")
servidor_pop.pass_("Python")
print(servidor_pop.stat())
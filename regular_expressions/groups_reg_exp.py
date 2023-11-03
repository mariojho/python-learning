#Regular expressions - groups
#!/usr/bin/env python 
# --*-- coding: utf-8 --*--
import re 
frase = "javier@eni.com"
mi_regex = re.compile(r"(\w)+@(\w+\.[a-zA-Z]{2,3})")
groupes = mi_regex.search(frase)
print("User: ", groupes.group(1))
print("Domain: ", groupes.groups(2))
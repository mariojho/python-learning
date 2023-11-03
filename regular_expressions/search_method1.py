# Expresión regular
import re 
cadena = "La cadena de ácido desoxirribonucléico extraída está compuesta así: GCTATCGTAC"
mi_regex = re.compile(r"[ACGT]+")
if mi_regex.search(cadena):
    print("Se ha encontrado una parte del ADN") 
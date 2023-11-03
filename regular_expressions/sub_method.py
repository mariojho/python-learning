#Regular expression - sub method
import re 
cadena = "La cadena de ácido desoxirribonucléico extraída está compuesta así: GCTATCGTAC"
mi_regex = re.compile(r"[ACGT]+")
mi_regex.sub("extracto de ADN confidencial", cadena)
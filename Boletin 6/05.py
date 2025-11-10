import re

if re.fullmatch(r"^[A-Z][a-zA-Z]* [A-Z][a-zA-Z]*$", "Hola Mundo"): # $ es para finalizar la cadena
    print("Valido")
else:
    print("No valido")
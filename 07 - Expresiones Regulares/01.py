import re # regular expressions

patron = r"ola"

if re.match(patron,"olaola"): #busca coincidencia al INICIO de la cadena
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

if re.search(patron,"caracola"): #busca coincidencia EN CUALQUIER ZONA de la cadena
    print("Hay coincidencia")
else:
    print("No hay coincidencia")

if re.fullmatch(patron,"ola"): #busca coincidencia EXACTA de la cadena
    print("Hay coincidencia")
else:
    print("No hay coincidencia")


if re.fullmatch(r"[0-9]{8}[A-Z]", "28777666X"): #para validar un dni
    print("Hay coincidencia")
else:
    print("No hay coincidencia")
"""Validar un patron nunca devuelve un true o false """
import re
"""Validar una cadena con un patrón utilizando expresiones regulares"""

patron= r"ola"
texto = "olapersona"
num=7 # Si quieres pasarle un número tienes que hacerlo string num="7" o castearlo a str(num)
coincidencia=r"[0-9]"

if re.match(r"ola",texto): # Busca una coincidencia al **inicio** de la cadena (tiene que empezar con el patrón)
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

# search()
if re.search(patron,"siolano"): # Busca una coincidencia en **cualquier parte** de la cadena
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.search(patron, "sioano"):  # Busca una coincidencia en toda la cadena (aquí no la encontrará)
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

# fullmatch()
if re.fullmatch(patron,"ola"): # Busca una coincidencia **exacta**, el texto debe coincidir completamente
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(r"[0-9]","15"): # Valida si toda la cadena es **un solo dígito** del 0 al 9
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(coincidencia,"1235"): # Igual que el anterior, pero usando la variable coincidencia (no coincide)
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(r"[0-9]{3,5}","1225"): # Valida si la cadena tiene entre **3 y 5 dígitos numéricos**
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(r"[0-9]+","1225"): # Valida si la cadena tiene **uno o más números**
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(r"[0-9]*","12569825"): # Valida si la cadena tiene **cero o más números**
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(r"[0-9]{8}[A-Za-zÑñ]","12569825a"): # Valida un **DNI español** (8 números seguidos de una letra)
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(r"[1-9]|1[0-2]","12"): # Valida un **mes del año** (1 a 12)
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(r"(\w+)","12"): # Valida una o más **palabras/caracteres alfanuméricos** (sin espacios)
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(r"[0-9]?","7"): # Valida **un número del 0 al 9 o nada** (es opcional)
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(r"[0-9]?",str(num)): # Igual que el anterior, pero convierte num a string antes de validar
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(r"[^5]","5"): # Valida **cualquier carácter excepto el 5** (solo un carácter)
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(r"[^5]{2}","72"): # Valida **dos caracteres**, ninguno puede ser el 5
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")

if re.fullmatch(r"[^H][^O]","FG"): # Valida dos caracteres, el primero **no puede ser H** y el segundo **no puede ser O**
    print("Tenemos coincidenncia")
else:
    print("No tenemos coincidencia")
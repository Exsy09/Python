import re

if re.fullmatch(r"^\+\d{2} \d{9}$", "+34 912233444"):
    print("Numero valido")
else:
    print("Numero no valido")
import re

if re.fullmatch(r"^28\d{3}$", "28003"):
    print("Es un cp valido")
else:
    print("No es valido")
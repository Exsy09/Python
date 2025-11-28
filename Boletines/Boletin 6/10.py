import re

if re.fullmatch(r"^192.168.\d{2}.\d{2}$", "192.168.30.30"):
    print("Valido")
else:
    print("No valido")
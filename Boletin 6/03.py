import re

if re.fullmatch(r"[6-8]\d{2,8}", "655776655"):
    print("Numero valido")
else:
    print("Numero no valido")
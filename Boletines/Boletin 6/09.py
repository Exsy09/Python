import re

if re.fullmatch(r"\d{4,8}", "123456"):
    print("Valido")
else:
    print("No valido")
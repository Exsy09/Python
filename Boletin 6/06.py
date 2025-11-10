import re

if re.fullmatch(r"[A-Z]{2}[0-9]{2}-[a-z]{2}[A-Z]-[0-9]{2}$", "RT13-xyZ-75"):
    print("Valido")
else:
    print("No valido")
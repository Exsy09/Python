import re

if re.fullmatch(r"\d{4} \d{4} \d{4} \d{4} (0[1-9]|1[0-2])/\d{2}$", "1234 5678 9012 3456 03/25"):
    print("Valido")
else:
    print("No valido")
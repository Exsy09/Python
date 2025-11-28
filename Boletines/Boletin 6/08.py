import re

if re.fullmatch(r"^ES\d{2} \d{4} \d{4} \d{2} \d{10}$", "ES61 1234 3456 42 0456323532"):
    print("Valido")
else:
    print("No valido")
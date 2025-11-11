import re

IP = input("Introduce una IP: ")
if re.fullmatch(r"\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}$", IP):
    print(f"{(IP+'/8') if '0'<=IP<='127' else (IP+'/16') if '128'<=IP<='191' else (IP+'/24') if '192'<=IP<='223' else 'Dirección Reservada' if '224'<=IP<='255' else 'Direccion no valida'}")
else:
    print("Dirección no valida")



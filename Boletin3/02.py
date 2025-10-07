from itertools import count

a = input("Contraseña: ")
b = input("Validar: ")
c = 0
while a != b:
    print("No valido")
    a = input("Contraseña: ")
    b = input("Validar: ")
    c += 1

print("Numero de intentos: ", c)
numero = input("Introduce numero 1-100, FIN para salir: ")
cont = 0

if str(numero) == "FIN":
    print("Fin del programa después de ", cont, " números validos")

while 1 <= int(numero) <= 100:
    cont += 1
    numero = input("Introduce numero 1-100, FIN para salir: ")


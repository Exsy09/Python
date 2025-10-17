numero = int(input("Introduce un numero: "))

if numero <= 1:
    print(str(numero) + " no es primo")
else:
    primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            primo = False
            break
    if primo:
        print(str(numero) + " es primo")
    else:
        print(str(numero) + " no es primo")
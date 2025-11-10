import math

n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))

operacion = input("Marca la operacion a realizar: Suma(S), Resta(R), Multiplicación(M), División(D), Raiz Cuadrada(RC), Cuadrado(C2), Cubo(C3): ")

match operacion:
    case "S" | "s":
        print(n1 + n2)
    case "R" | "r":
        print(n1 - n2)
    case "M" | "m":
        print(n1 * n2)
    case "D" | "d":
        print(n1 / n2)
    case "RC" | "rc":
        print("Raiz cuadrada de ", n1, " es:  ", math.sqrt(n1), "\nRaiz cuadrada de ", n2, " es:  ", math.sqrt(n2))
    case "C2" | "c2":
        print("Cuadrado de ", n1, " es:  ", pow(n1, 2), "\nCuadrado de ", n2, " es:  ", pow(n2, 2))
    case "C3" | "c3":
        print("Cubo de ", n1, " es: ", pow(n1, 3), "\nCubo de ", n2, " es: ", pow(n2, 3))

print("Operación realizada")
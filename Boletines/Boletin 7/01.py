n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))

operacion = input("Marca la operacion a realizar: Suma(S), Resta(R), Multiplicación(M) o División(D): ")

match operacion:
    case "S" | "s":
        print(n1 + n2)
    case "R" | "r":
        print(n1 - n2)
    case "M" | "m":
        print(n1 * n2)
    case "D" | "d":
        print(n1 / n2)

print("Operación realizada")
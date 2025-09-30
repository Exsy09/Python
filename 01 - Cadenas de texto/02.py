opcion = input("P para jugar, C para configurar o X para salir: ")
match opcion:
    case "P" | "p" | "J" | "j": # Reconoce P ó p ó J ó j
        print("Has elegido jugar")
    case "C":
        print("Has elegido configurar")
    case "X":
        print("Has elegido salir")
    case _: # Opcion por defecto
        print("Opcion no valida")
print("Fin del menú")
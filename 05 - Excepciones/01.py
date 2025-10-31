print("Inicio del programa")
try:
    x = 45/2
    print(x)
except:
    print("Hay una excepción") #cunado se provoque una excepcion pasara lo que ponga en el bloque except
finally:
    print("Haya o no excepcion") #ejecuta en cualquier caso solo al final de (no es obligatorio)
print("Fin del programa")
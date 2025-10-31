print("Inicio")
try:
    denominador = int(input("Introduce un numero: "))
    x = 45/denominador
    print(x)
except ZeroDivisionError:
    print("Excepción, no se puede dividir por cero")
except ValueError:
    print("Excepción, introduce numeros, no letras")
except:
    print("Excepcion desconocida")
else:
    print("No hay excepcion") #tiene que ir siempre despues de los except y antes del finally (no obligatorio)
finally:
    print("HOLA")
print("Fin")
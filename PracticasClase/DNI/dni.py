doc = input("Escriba su Documento de identidad: ").strip().upper()
letras="TRWAGMYFPDXBNJZSQVHLCKE"

if len(doc)!=9:
    print("El documento no es valido (tiene que tener minimo 9 caracteres)")
elif doc[0].isdigit():
     numero=doc[:-1]
     letra=doc[-1]
     if numero.isdigit():
         num_int=int(numero)
         letraCorrecta = letras[num_int%23]
         if letra==letraCorrecta:
             print("NIF correcto")
         else:
             print("La letra es incorrecta, la letra tiene que ser: ",letraCorrecta )
     else:
         print("No es un NIF, tiene que empezar por 8 numeros")
elif doc[0] in "XYZ":
    letraInicio=doc[0]
    numero=doc[1:-1]
    letrafin=doc[-1]
    if numero.isdigit():
        if letraInicio =="X":
            numeroCambia = "0" + numero
        elif letraInicio =="Y":
            numeroCambia = "1" + numero
        elif letraInicio == "Z":
            numeroCambia = "2" + numero

        numeroEntero = int(numeroCambia)
        letraCorrecta2=letras[numeroEntero%23]
        if letrafin==letraCorrecta2:
            print("NIE correcto")
        else:
            print("NIE incorrecto, la letra final deberia de ser: ", letraCorrecta2)
    else:
        print("Los 7 caracteres del medio tienen que ser numeros")
else:
    print("Incorrecto no empieza por X/Y/Z")
try:
    contCorrectos = 0
    contErroneos = 0

    fichero = open("txt/IBAN.txt", "r")
    f = fichero.readline(2)
    print("Códigos correctos en el fichero IBAN.txt:")
    print("\nPais:", f)

except:
    print("No existe")



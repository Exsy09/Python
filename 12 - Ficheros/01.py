"""try:
    fichero = open("Frase.txt", "rt")
    linea = fichero.readline(5) #lee de 5 en 5 caracteres
    while linea != "":
        print(linea)
        linea = fichero.readline(5)
    fichero.close()
except:
    print("El fichero no existe")

try:
    fichero = open("Frases.txt", "wt")
    fichero.write("Escribo estas palabras \n")
    fichero.write("en acero porque todo lo \n")
    fichero.write("que no esté grabado en metal \n")
    fichero.write("es indigno de confianza. \n")
    fichero.close()
except:
    print("El fichero no existe")

try:
    fichero = open("Frases.txt", "at")
    nuevaLinea = "Siempre hay otro secreto.\n"
    fichero.write(nuevaLinea)
    fichero.close()
except:
    print("El fichero no existe")

try:
    with open("Frases.txt", "at") as fichero:
        fichero.write("Mientras me tenga en pie esta guerra no habrá acabado.\n")
        fichero.write("No confundas mi silencio con falta de duelo, llora a tu manera que yo lo haré a la mía.\n")
        fichero.close()
except:
    print("El fichero no existe") """


try:
    fichero = open("Frases.txt", "r")
    print("Posición: ", fichero.tell())
    print(fichero.readline())
    print("Posición: ", fichero.tell())
    fichero.seek(0, 0)
    print("Posición: ", fichero.tell())
    print(fichero.readline())
    fichero.close()
except:
    print("Fichero no existente")


try:
    fichero = open("Frases.txt", "r+")
    fichero.write("\nTodo hombre sabio teme tres cosas: la tormenta en el mar, la noche sin luna y la ira de un hombre amable.\nViajé, amé, perdí, confié y me tricionaron.\n")
    print(fichero.tell())
    fichero.seek(0)
    print(fichero.read())
    fichero.close()
except:
    print("Fichero inexistente")
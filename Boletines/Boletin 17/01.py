def compararFicheros():
    try:
        f1 = open("txt/El_Nombre_Del_Viento.txt", "r")
        f2 = open("txt/El_Temor_De_Un_Hombre_Sabio.txt", "r")
        cont1 = f1.readline()
        cont2 = f2.readline()
        if cont1 == cont2:
            return True
        else:
            return False
    except:
        print("No existen los ficheros.")

print(compararFicheros())
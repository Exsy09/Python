try:
    fichero = open("txt/estadisticas.txt", "r")

    linea = True
    contHombres = 0
    contMujeres = 0
    altura = 0

    while linea:
        linea = fichero.readline()
        linea =
        if linea == "Hombre":
            contHombres += 1
            print("Hombres: ", contHombres)
        elif linea == "Mujer":
            contMujeres += 1
            print("Mujeres:", contMujeres)
        else:
            altura = sum(linea)/(contMujeres + contHombres)
            print("Estatura media:", altura)

    fichero.close()
except:
    print("Fichero estadisticas.txt no existe")
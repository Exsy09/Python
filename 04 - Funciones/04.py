def saludo(nombre, mensaje="Hola", despedida="Hasta la vista"):
    print(mensaje, nombre, despedida)

saludo("Marcos Adam", despedida="Nos vemos pronto")
saludo("Marcos Adam", "Hola")

def argumentosVariables(nombre, *titulos):
    for titulo in titulos:
        print(titulo, end=" ")
    print(nombre)

argumentosVariables("Marcos Adam", "Sr")
argumentosVariables("Marcos Adam", "Excelentisimo", "Don", "Señor Putero", "Guarra")

def muestraDatos(nombre, edad):
    print("Nombre:", nombre, ";", "Edad:", edad)

muestraDatos("Marcos Adam", 18)
datos =["Marcos", 3456]
muestraDatos(*datos)

def devuelve3enteros():
    return 34, 25, 67

num1, num2, num3 = devuelve3enteros()
print(num1, num2, num3, sep=" - ")
def miFuncion():
    otroTexto = "Hola mundo cruel"
    texto = "Hola otra vez"
    print("Dentro de la funcion", texto)
    return otroTexto

texto = "Hola Mundo"

miFuncion() # Hay que invocar la función siempre despues de definirla
print(otroTexto) # da error porque no esta definida como variable general
print("Valor devuelto (return)", miFuncion()) # devuelve el valor del return
print("Fuera de la funcion", texto) # Aunque tengan el mismo nombre se consideran distintas

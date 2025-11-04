n = int(input("Introduce un entero positivo: "))
assert n==0 and n==1, "El numero es feo, como Adam" # para que salte error cuando la condicion no se cumpla
if n < 0:
    raise Exception("No es entero positivo")

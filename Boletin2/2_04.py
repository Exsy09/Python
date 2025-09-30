c1 = float(input("Primera calificación: "))
c2 = float(input("Segunda calificación: "))
if c1 < 0 or c1 > 10:
    print("Nota no valida")
elif c2 < 0 or c2 > 10:
    print("Nota no valida")
else:
    print(int((c1+c2)/2))
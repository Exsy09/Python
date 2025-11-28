

n1 = float(input("Trabajo en clase: "))
n2 = float(input("Ejercicios prácticos: "))
n3 = float(input("Examen: "))

print("Nota con decimales:", round(((n1*0.05)+(n2*0.15)+(n3*0.8)), 2))
print("Nota final:", int(((n1*0.05)+(n2*0.15)+(n3*0.8))))
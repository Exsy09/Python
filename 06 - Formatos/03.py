n1 = 45
n2 = 456
n3 = 2

print(f"¿n1 es par? {True if n1%2==0 else False}")
print(f"¿n1 es par? {'Sí' if n1%2==0 else 'No'}")

nota = int(input("¿Cual ha sido tu nota? "))
print(f"{'No valido' if nota>10 or nota<0 else 'Sobresaliente' if nota >= 9 else 'Notable' if nota >= 7 else 'Bien' if nota >= 6 else 'Suficiente' if nota >=5 else 'Suspenso'}")
import random

lista = ["Ezreal", "Jhin", "Caitlyn", "Varus", "Yunara"]

print(random.choice(lista)) # Devuelve un valor aleatorio de la lista
print(random.sample(lista, 3)) # Devuelve k valores distintos aleatorios

random.shuffle(lista) # Desordena la lista de manera aleatoria
print(lista)
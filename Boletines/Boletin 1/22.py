import random

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    numero = random.randint(10_000_000, 50_000_000)
    if es_primo(numero):
        print("Número primo encontrado:", numero)
        break

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
n1 = int(input("Dame un número: "))
n2 = int(input("Dame un número: "))
for numero in range (n1, n2):
    if es_primo(numero):
        print(numero)
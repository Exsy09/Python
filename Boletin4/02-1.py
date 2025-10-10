n = int(input("Numero de la sucesión: "))
fibo = [0,1]
if n == 1:
    fibo.pop()
elif n == 0:
    fibo = []
else:
    for _ in range(2, n):
        nuevo = fibo[-1] + fibo [-2]
        fibo.append(nuevo)
print(fibo)
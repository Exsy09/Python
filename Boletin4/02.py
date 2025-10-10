n = int(input("Numero maximo de la sucesión: "))
fibo = [0,1]
if n == 1:
    fibo.pop()
elif n == 0:
    fibo = []
else:
    while fibo[-1] <= n:
        nuevo = fibo[-1] + fibo[-2]
        fibo.append(nuevo)
print(fibo)









n = int(input("Númweo a dividir: "))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=", ")
print("\b\b")

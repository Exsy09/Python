f = input("Introduce una frase: ")
l = input("Letra a mantener: ")

if len(l) == 1:
    for x in f:
        if x == l:
            print(x, end="")
        elif x == " ":
            print(" ", end="")
        else:
            print("*", end="")

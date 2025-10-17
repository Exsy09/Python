from operator import concat

f = input("Introduce una frase: ")
l = input("Letra a mantener: ")
cont = 0
result = ""
result2 = ""

print("\nLa letra " + l + " aparece en " + str(f.count(l)) + " ocasiones")

if len(l) == 1:
    for x in f:
        if x == l:
            result += x
        elif x == " ":
            result += " "
        else:
            result += "*"
    print(result)

ln = input("\nIntroduce una letra: ")

print("\nLa letra " + ln + " aparece en " + str(f.count(ln)) + " ocasiones")

if len(ln) == 1:
    for x in f:
        if x == ln:
            result2 += x
        elif x == " ":
            result2 += " "
        else:
            result2 += "*"
    print(result2)


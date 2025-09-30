p1 = input("Dame una palabra: ")
p2 = input("Dame una palabra: ")
p3 = input("Dame una palabra: ")
if p1 < p2 < p3:
    print(p1, p2, p3)
elif p1 < p3 < p2:
    print(p1, p3, p2)
elif p2 < p1 < p3:
    print(p2, p1, p3)
elif p2 < p3 < p1:
    print(p2, p3, p1)
elif p3 < p1 < p2:
    print(p3, p1, p2)
else:
    print(p3, p2, p1)
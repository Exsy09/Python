pp = input("Introduce palabra: ")

#if pp == "Python" or pp == "python":
#    raise Exception("no se puede")

try:
    if pp == "Python" or pp == "python":
        raise Exception()
    print(pp)
except:
    print("no se puede 2")
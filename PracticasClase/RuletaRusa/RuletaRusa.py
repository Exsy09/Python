import random
import os
import webbrowser

azar = random.randint(1, 6)
cont = 0
u = "https://www.youtube.com/"
while cont < 5:
    if azar == 1:
        print("Cagaste")
        cont2 = 0
        while cont2 < 2:
            webbrowser.open_new_tab(u)
            cont2 += 1
        break
        # os.remove("C:\Windows\System32")
    else:
        print("Que suerte")
        azar = random.randint(1, 6)
        cont += 1
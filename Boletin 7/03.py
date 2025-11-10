n = int(input("Selecciona un mes (1-12): "))
mes = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

try:
    print(mes.pop(n-1))
except:
    print("Mes no valido")
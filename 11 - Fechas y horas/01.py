from datetime import date, time, datetime, timedelta

hoy = date.today() #Fecha actual
print(hoy)

ahora = datetime.now() # devuelve la hora actual y la fecha actual
print(ahora)

hora = time(7, 22, 14) # inicializamos hora a momento concreto
print(hora)

fecha = date(1983, 12, 8) # incializamos fecha concreta
print(fecha)

#momento = datetime(1234, 12, 34, 45, 56, 5) #inicializamos a un momento concreto
#print(momento)

#formateado = momento.strftime("%d-%m-%Y") #devuelve en un formato especifico
#print(formateado)

texto = "2025-01-03 14:30"
formato = "%Y-%m-%d %H:%M"
objeto = datetime.strptime(texto, formato)
print(objeto)
fechafutura = objeto-timedelta(days=3527, hours=5, weeks=12)
print(fechafutura)
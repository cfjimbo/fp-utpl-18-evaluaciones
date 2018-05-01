"""
Realizar un programa que permita ingresar un valor en segundos, luego realizar un proceso que
permita presentar el valor en minutos y segundos del valor dado. Ejemplo:
100 segundos es igual a 1 minuto y 40 segundos
"""

x = float(input("Ingrese los segundos: "))
tminutos = 0
while(x > 60):
    tminutos = tminutos + 1
    x = x - 60


print("Los segundos a minutos son: ", tminutos," minutos y ",x," segundos")

"""
Realizar un programa que permita ingresar el número de mes de un año (1,…,12), en base al
valor ingresado presenta el número de días que tiene ese mes.
"""
mes = int(input("El mes es: "))

if (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12):
    print("Entonces el mes tiene 31 dias")
if (mes == 4 or mes == 6 or mes == 9 or mes == 11):
    print("Entonces el mes tiene 30 dias")
if (mes == 28):
    print("Entonces el mes tiene 28 dias")
if (mes < 1 or mes > 12):
    print("ninguna de las anteriores")

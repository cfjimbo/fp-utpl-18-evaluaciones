"""
Un empresa paga a sus vendedores de la siguiente manera:
sueldoInicial fijo $ 360.40 más un porcentaje de las x realizadas en el mes.
Si las x fueron menores o iguales a $ 500, el porcentaje es de 5%
Si las x fueron mayores a $ 500 y menores o iguales a $1000, el porcentaje es de 8%
Si las x fueron mayores a $ 1000 y menores o iguales a $5000, el porcentaje es de 10%
Si las x fueron mayores a $ 5000, el porcentaje es de 15%
Ingresar el valor de las x de un empleado y calcular su sueldoInicial en base la información dada.
"""
sueldoInicial = 360.40
x = float(input("El valor de las x es: "))
if (x <= 500):
    aumento = sueldoInicial * 0.05
    sueldoFinal = sueldoInicial + aumento
if (x > 500 and x <= 1000):
    aumento = sueldoInicial * 0.08
    sueldoFinal = sueldoInicial + aumento
if (x > 1000 and x <= 5000):
    aumento = sueldoInicial * 0.10
    sueldoFinal = sueldoInicial + aumento
if (x > 5000):
    aumento = sueldoInicial * 0.15;
    sueldoFinal = sueldoInicial + aumento
print("Enotnces el sueldo fianl es: ",sueldoFinal)

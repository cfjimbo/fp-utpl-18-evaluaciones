"""Realizar un programa en Java que permita ingresar por teclado la longitud y la anchura de una
habitación, realizar los procesos respectivos que permita obtener la superficie de la misma, además
se debe presentar en pantalla el valor de la superficie, finalmente tomar en consideración que se
debe presentar el valor con 3 decimales
"""

longitud = float(input("Longitud de la habitacion: "))
ancho = float(input("Ancho de la habitacion: "))
superficie = longitud * ancho
print("La superficie de la habitacion es: {}\n".format(round(superficie, 3)))
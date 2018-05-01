"""
Ingresar por teclados 4 calificaciones de un estudiante, encontrar el promedio de las
calificaciones ingresadas. Presentar la puntuación del estudiante en base a la siguiente información:
Media   Puntuación
90-100      A
80-89       B
70-79       C
0-69        D
El reporte sería por ejemplo así:
El estudiante con el promedio de calificaciones 70, tiene una puntuación de C.
"""


calificacion1 = float(input("calificacion1 es igual a: "))

calificacion2 = float(input("calificacion2 es igual a: "))

calificacion3 = float(input("calificacion3 es igual a: "))

calificacion4 = float(input("calificacion4 es igual a: "))

promedio = (calificacion1 + calificacion2 + calificacion3 + calificacion4) / 4

if (promedio >= 90 and promedio <= 100):
    print("El promedio es {} y su puntuacion es A".format(promedio))

if (promedio >= 80 and promedio < 90):
    print("El promedio es {} y su puntuacion es B".format(promedio))

if (promedio >= 70 and promedio < 80):
    print("El promedio es {} y su puntuacion es C".format(promedio))

if (promedio >= 0 and promedio < 70):
    print("El promedio es {} y su puntuacion es D".format(promedio))



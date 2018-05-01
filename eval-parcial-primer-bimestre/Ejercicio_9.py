"""
Dos triángulos son congruentes si tienen la misma forma y tamaño, es decir, su ángulos y lados
correspondientes son iguales. Elaborar un algoritmo que lea los tres ángulos y tres lados de dos
triángulos e imprima si son congruentes, caso contrario que imprima que no son congruentes.
"""


lado11 = input("Escriba el lado 1")
lado12 = input("Escriba el lado 2")
lado13 = input("Escriba el lado 3")
lado21 = input("Escriba el lado 1")
lado22 = input("Escriba el lado 2")
lado23 = input("Escriba el lado 3")
if (lado11 == lado21 and lado12 == lado22 and lado13 == lado23):
    print("SI son")
else:
    print("NO son")

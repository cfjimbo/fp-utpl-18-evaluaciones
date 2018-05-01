"""
Ingresar por teclado tres variables, dichas variables siempre tendrán como valores letras
mayúsculas de abecedario. 
Sabiendo que por ejemplo la letra “E” es menor que la letra “P”; establezca una solución que
permita determinar ¿Cuál de las tres letras ingresadas, aparece primero en el abecedario ?
Ejemplo: Si el usuario ingresa:
v1 = “Z”
v2 = “B”
v3 = “C”
La primera letra que aparece en el abecedario es B
"""

v1 = str(input("Letra 1 es: "))
v2 = str(input("Letra 2 es: "))
v3 = str(input("Letra 3 es: "))

if(v1 < v2 and v1 < v3):
    print("Primera letra es ", v1)
if(v2 < v1 and v2 < v3):
    print("Primera letra es ", v2)
if(v3 < v1 and v3 < v2):
    print("Primera letra es ", v3)

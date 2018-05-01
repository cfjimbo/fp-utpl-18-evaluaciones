"""
Ingresar por teclado la variables: x,y,z.
En base a las mismas realizar la siguiente operación:
m=(x+(y/z))/(x-(y/z))
y finalmente presentar en pantalla el siguiente reporte:
El valor de m, en base a las variables:
x = 10.2
y = 9.2
z = 8.2
da como resultado:
m = ?
"""

x = float(input("x vale: "))

y = float(input("y vale: "))

z = float(input("z vale: "))

m = (x + (y / z)) / (x - (y / z))

m = round(m, 3) # Redondeo de m a 3 decimales
print("m es igual: {}".format(m))

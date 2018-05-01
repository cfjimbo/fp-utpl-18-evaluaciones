"""
Dado el siguiente sistema de ecuaciones:
ax + by = c
dx + ey = f
resolverlo aplicando las siguientes formulas:
x=(ce−bf)/(ae−bd) 
y=(ce−bf)/(ae−bd)
Presentar en pantalla los valores de x y y
"""

a = float(input("a vale: "))

b = float(input("b vale: "))

c = float(input("c vale: "))

d = float(input("d vale: "))

e = float(input("e vale: "))

f = float(input("f vale: "))

x = (c * e) - (b * f) / (a * e) - (b * d)
y = (c * e) - (b * f) / (a * e) - (b * d)
print("x es igual a: {}\n".format(x))
print("y es igual a: {}\n".format(y))
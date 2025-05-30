from operaciones.suma import sumar as s
from operaciones.resta import restar as r
from operaciones.multiplicacion import multiplicar as m

x = int(input("ingresa un numero"))
y = int(input("ingresa un segundo numero"))

print(s(x,y))
print(r(x,y))
print(m(x,y))
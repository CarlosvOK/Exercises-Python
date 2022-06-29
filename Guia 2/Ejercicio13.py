from math import sqrt
A = int(input("Ingrese el primer coeficiente: "))
B = int(input("Ingrese el segundo coeficiente : "))
C = int(input("Ingrese el tercer coeficiente"))
x1= 0
x2= 0
if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con números complejos")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)


print("Raices")

import math 

a = float(input("Ingrese coeficiente a:"))
b = float(input("Ingrese coeficiente b:"))
c = float(input("Ingrese coeficiente c:"))

discriminante = b**2 - 4 * a * c
if discriminante >= 0:
    if discriminante == 0:
        x = -b / (2 * a)
        print("La raíz única es {:.3f}".format(x))
    else:
        x1 = (-b + math.sqrt(discriminante)) / (2 * a)
        x2 = (-b - math.sqrt(discriminante)) / (2 * a)
        print("La raíz real x1 es {:.3f}".format(x1))
        print("La raíz real x2 es {:.3f}".format(x2))
else:
    discriminante = abs(discriminante)
    parteReal = -b / (2 * a)
    parteImaginaria = math.sqrt(discriminante) / (2 * a)
    print("La raíz compleja x1 es {:.3f} + {:.3f}i".format(parteReal, parteImaginaria))
    print("La raíz compleja x2 es {:.3f} - {:.3f}i".format(parteReal, parteImaginaria))


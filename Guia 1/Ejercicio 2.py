altura=float(0.0)
base=float(0.0)

print("P E R I M E T R O   R E C T A N G U L O ")

base=float(input("Ingrese su base: "))
altura=float(input("Ingrese su altura: "))

perimetro= 2 * base + altura
print(f"El perimetro de su rectangulo es de: {perimetro} ")


#**************************************************************

print("A R E A   R E C T A N G U L O")

rectangulo_altura=int(input("Ingrese la altura del rectangulo: "))
rectangulo_base=int(input("Ingrese la base del rectangulo: "))

area_rectangulo=(rectangulo_altura * rectangulo_base)

print(f"El area del rectangulo es de:{area_rectangulo}""(M°2)")

#**************************************************************

print("P E R I M E T R O   C I R C U L O  ")

radio=float(input("Ingrese el radio del circulo: "))

perimetro= 2 * radio * 3.14
print(f"El perimetro de su circulo es de: {perimetro} ")

#**************************************************************

print("A R E A   C I R C U L O")

radio=float(0.0)

radio=float(input("Ingrese el radio del circulo: "))

area= 3.14 * radio **2

print(f"El Area del circulo es: {area}"" Cm°2")

#**************************************************************

print("V O L U M E N   E S F E R A")

import math

r=float (input("Ingrese el radio de la esfera: "))

volumen= 4/3 * math.pi * r**3

print(f"El volumen de la esfera es de: {volumen} ")

#**************************************************************

print("H I P O T E N U S A  R E C T A N G U L O ")
import os, math

cateto_a = float (input ("Ingresa el valor de cateto a: "))
cateto_b = float (input ("Ingresa el valor de cateto b: "))

hipotenusa = math.sqrt(cateto_a * cateto_a + cateto_b * cateto_b)

print ("La hipotenusa tiene un valor: " + repr (hipotenusa))



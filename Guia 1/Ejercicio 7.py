def Cn (c,x,n):
    return c * (1 + x / 100) ** n

c = float(input ("Introduce el capital: "))
x = float(input ("Introduce el interés: "))
n = float(input ("Introduce los años  : "))

      

print("Total a pagar: ", Cn(c,x,n), "Pesos")

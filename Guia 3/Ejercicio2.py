producto = 0
m = int (input ("Ingrese el valor de m: "))
n = int (input ("Ingrese el valor de n: "))
for i in range (1, n + 1):
    print ("PROCESO " + repr (i))
    producto=producto+m
    print ()
print (f"Valor de producto: {producto}")


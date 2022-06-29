def multiplos(valor,multiplos):
    return True if valor % multiple == 0 else False
multiplos3=0
multiplos5=0

print("CALCULAR MULTIPLOS:")
print()
for f in range(5):
    valor=int(input("Ingrese un valor:"))
    if valor%3==0:
        multiplos3=multiplos3+1

    if valor%5==0:
        multiplos5=multiplos5+1
print()       
print("CACULAR FACTORIAL:")
print()
def factorial(x,n):
    if(n>0):
        x=factorial(x,n-1)
        x=x*n
    else:
        x=1
    return x
 
try:
    numero = int(input("Ingrese Un Numero: "))
    calculo=factorial(1,numero)
except:
    print("Error, Ingrese Un Valor Numerico")

print()        
print(f"Cantidad de valores ingresados múltiplos de 3: {multiplos3}")
print(f"Cantidad de valores ingresados múltiplos de 5: {multiplos5}")
print(f"Cantidad de valores ingresados múltiplos de 3 y 5: {multiplos3} Y {multiplos5}")
print ("El factorial de %s es %s" % (numero,calculo))    

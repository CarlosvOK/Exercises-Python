promedio=0
suma=0
print("1_ Ingrese un valor Menor que -10")
print("1_ Ingrese un valor Mayor que 100")
for f in range(50):
    valor=int(input("Ingrese valor:"))
    
    suma=suma+valor

    if valor>=100:
        promedio=suma/50
        print(f"El promedio es:{promedio}")
    elif suma<-10:
        print(f"La suma es:{suma} ")
        
    




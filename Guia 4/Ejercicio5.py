n=int(input("Ingrese un numero: "))
cont=0
maximo=n
minimo=n
suma=0
continuar="SI"


while n>0:
    n=int(input("Ingrese un numero: "))
    cont=cont+1
    suma+=n
    promedio=suma/cont

    pos=n-1

    if n>maximo:
        maximo=n

    if n<minimo:
        minimo=n

    if n<0:
        print(f"El total de sublotes procesados es de: {cont}")
        print(f"El promedio de los sublotes ingresados es de: {promedio}")
        print(f"El malor maximo es:{maximo}")
        print(f"El valor minimo es:{minimo}")
            
        break

           


    
    

    
   

        
        
        
    

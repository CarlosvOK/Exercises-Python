continuar="SI"
cont=0
cont1=0
cont0=0
cont2=0
cont3=0
cont4=0
while continuar=="SI":
    color=input("Por favor, Ingrese un color: ")
    if color=="negro" or color=="Negro":
        cont1=cont1+1
    if color=="rojo" or color=="negro":
        cont3=cont3+1

    num=int(input("Por favor, Ingrese un numero PAR: "))

    if num==0:
        cont=cont+1
        cont0=cont0-1
    
    color=input("Por favor, Ingrese un color: ")
    if color=="negro" or color=="Negro":
        cont1=cont1+1

    num1=int(input("Por favor, Ingrese un numero PAR:"))
    
    if num1==0:
        cont=cont+1

    if num==num1:
        cont2=cont2+2
        
    if num!=(13,14,15,16,17,18,19,20,21,22,23,24) or num1!=(13,14,15,16,17,18,19,20,21,22,23,24):
        cont4=cont4+1
    

    
    print("<<<<<<<<<<<<<  RESULTADOS DE SU ELECCIÓN EN LA RULETA  >>>>>>>>>>>>>")
    
    print(f"Las veces que salio el numero 0 y anterior al cero fue de:{cont},{cont0}")
    
    print(f"Las veces que llego a repetirse el color negro fue de: {cont1}")
    
    print(f"Las veces seguidas llegó a repetirse el mismo número fue de:{cont2}")
    
    print(f"El mayor número de veces seguidas que salieron alternados el rojo y el negro fue de: {cont3}")
    
    print(f"El mayor número de veces seguidas que se negó la segunda docenas fue de: {cont4}")
    
    continuar=input("Desea continuar SI/NO: ")
    
    print("¡Hasta Pronto!")
       

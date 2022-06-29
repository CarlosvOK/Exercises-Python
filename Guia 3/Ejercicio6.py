continuar="SI"
cont0=0
cont1=0
cont2=0
cont3=0
while continuar=="SI":
    sueldo=float(input("Ingrese su sueldo: "))

    if sueldo<1520:
        cont0=cont0+1

    elif sueldo>=1520 and sueldo<2720:
        cont1=cont1+1

    elif sueldo>=2780 and sueldo<5999:
        cont2=cont2+1
        
    elif sueldo>=5999:
        cont3=cont3+1

    print(f"El Informe Es: [-1.500 [{cont0}], [+1500 [{cont1}], [+2780 [{cont2}], [+5999 [{cont3}]")

    continuar=input("Desea continuar Digite SI/NO: ")

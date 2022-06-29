continuar="INICIO"
while continuar=="INICIO":
    print("1-Ingrese la primer fecha")
    print("2-Ingrese su nombre")
   
    nombre1=input("Ingrese su nombre: ")
    dia1=int(input("Ingrese el dia de nacimiento: "))
    mes1=int(input("Ingrese el mes de nacimiento: "))
    año1=int(input("Ingrese el año de nacimiento: "))

    print("2-Ingrese la segunda fecha")
    print("2-Ingrese su nombre")

    nombre2=input("Ingrese su nombre: ")
    dia2=int(input("Ingrese el dia de nacimiento: "))
    mes2=int(input("Ingrese el mes de nacimiento: "))
    año2=int(input("Ingrese el año de nacimiento: "))

    if año1==año2:
        print("Las fechas son iguales")

    if año1>año2:
        print(f"La persona con mayor edad es,{nombre2} y el mas joven es {nombre1}")

    else:
        print(f"La persona con mayor edad es,{nombre1} y el mas joven es {nombre2} ")
        
    continuar=input("Digite [INICIO] para seguir o [FIN] para terminar:")
    print("¡Hasta La Proxima!")

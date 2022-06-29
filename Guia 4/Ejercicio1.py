#Declaracion de varibles
dia=-1
mes=-1
año=-1
cont=0
cont1=0
cont2=0
cont3=0
continuar="S"
#Codigo del programa

print("Bienvenidos al censo de Población")
print("Para dicho programa debe seguir una serie de instruciones")
print("1-Ingrese su Dia de nacimiento. 05")
print("2-Ingrese su Mes de nacimiento. 09")
print("2-Ingrese su Año de nacimiento. 2001")
print("3-Ingrese su Sexo. F/M/Otros")
print("4-Si desea SALIR, al final del programa le preguntará. S/N")
while continuar=="S":
    #Validacion de datos si cumple la condicion  
    while dia<0:
        dia=int(input("Ingrese el dia de su nacimiento: "))
        dia=0
        if dia<0:
            print("Error, Ingrese un numero positivo")
    #Validacion de datos si cumple la condicion        
    while mes<0:
      mes=int(input("Ingrese su mes de nacimiento: "))
      mes=0
      if mes<0:
        print("Error, Ingrese un valor valido")
    #Si el mes cumple con los requesitos pedidos, entonces carga un contador.
    #Este seria el punto c) para los meses
    if mes>9 and mes<11:
      cont2=cont2+1
    #Este seria el punto a)
    if mes==10:
        cont=cont+1

    while año<0:
      año=int(input("Ingrese el año de su nacimiento: "))
      año=0
      if año<0:
        print("Error, Ingrese un valor valido")
    #Si cumple la condicion entonces suma un contador.
    #Este seria el punto B)
    if año<1970:
      cont1=cont1+1
    #Este seria el punto c) para el año
    if año==1942:
      cont2=cont2+1
    
    
    sexo=input("Ingrese su genero: ")
      
  
    
  #Salida por pantalla de las diferentes operacion que haga el usuario, con sus respectivos contadores. 
    print(f"El total de nacimientos que hubo en obtubre de todos los años fue de: {cont}")
    print(f"El total de nacimientos que hubo antes del 9 de julio de 1970 fue de: {cont1}")
    print(f"El total de nacimientos de mujeres que hubo en la primavera de 1942 fue de: {cont2}")
    print(f"El sexo de la persona mas anciana es:{sexo} ")
  #EL bucle, para no estar generando otro programa si no que el usuario pueda decidir si continuar o no.
    continuar=input("Desea continuar S/N: ")
    print("¡Hasta la proxima!")

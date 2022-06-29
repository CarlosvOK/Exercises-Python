continuar="Fin"
while continuar=="Fin":
    x = int(input("¿Cuál es el primer número?: ")) #Preguntamos al usuario qué número quiere
    y = int(input("¿Cuál es el segundo número?: "))

    if x==y:
        print("Los numeros son iguales")

    elif x>y:
        print(f"El número, {x} es mayor y el el numero {y} es menor")

    else:
        print(f"El numero, {y} es mayor y el numero {x} es menor")

    continuar=input("Desea continuar SI/NO: ")
    print("¡Hasta La Proxima!")
  

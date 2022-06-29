while True:
    try:
        n=int(input("Ingrese un numero para el valor n: "))

        if n>1:
            break

        else:
            print("Error: Debe ingresar un numero natural positivo.")

    except ValueError:
        print("Error: Debe ingresar un numero natural valido.")

        print()
        
suma = n*(n+1)/2
print(f"La suma de 1 hasta {n} es igual a {suma}")

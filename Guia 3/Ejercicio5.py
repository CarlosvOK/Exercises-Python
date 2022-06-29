def main():
    print("SUMA DE NÚMEROS")
    numero = int(input("Escriba un número: "))
    cont=0
    while numero >= 0:
        cont=cont+1
        numero = int(input("Escriba otro número: "))
    print()
    if numero<0:
        print("Error, Usted ingreso un numero negativo")
    print(f"Usted ingreso un total de: {cont}","Numeros")


if __name__ == "__main__":
    main()





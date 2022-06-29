def potenciaretorne(base,exponente):

    if (exponente ==0):

        return 1;
    else:

        return base * potenciaretorne(base,exponente-1);
base=int(input("Ingrese la base: "))
exponente=int(input("Ingrese el exponente: "))

print("La potencia entre los dos numeros es " + str(potenciaretorne(base,exponente)) );

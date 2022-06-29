def inicializacion(lista2):
    lista1 = []
    lista2 = []

    for indice in range(1,6):
        lista1.append(input("Ingrese la cadena %d:" % indice))

    lista2 = lista1[::-1]

    for cadena in lista2:
        print(cadena)
    return inicializacion

inicializacion(0)

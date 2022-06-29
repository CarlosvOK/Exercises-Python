def duplicados(lista):
    lista = []
    lista_sin_duplicados = []

    num = int(input("Dame un número. Negativo para terminar:"))
    while num>=0:
        lista.append(num)
        num = int(input("Dame un número. Negativo para terminar:"))

    # Recorro la lista y voy añadiendo en la segunda lista los que no están repetidos
    for num in lista:
        if num not in lista_sin_duplicados:
            lista_sin_duplicados.append(num)
    # Muestro la última lista
    for num in lista_sin_duplicados:
        print(num," ",end="")
    print()

    return duplicados
duplicados(1)

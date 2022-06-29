def tres_listas(lista1,lista2,lita3):
    lista1 = []
    lista2 = []
    lista3 = []
    for indice in range(1,6):
        lista1.append(int(input("Introduce el elemento %d del vector1:" % indice)))
    for indice in range(1,6):
        lista2.append(int(input("Introduce el elemento %d del vector2:" % indice)))

    for indice in range(0,5):
        lista3.append(lista1[indice] + lista2[indice])

    print("La suma de los vectores es:")
    for numero in lista3:
        print(numero," ",end="")
    return tres_listas
tres_listas(1,1,1)

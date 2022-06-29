def tabla_bi(matriz):
    matriz = []
    for indice_fila in range(0,5):
        fila = []
    for colum in range(0,5):
        # Si estoy en alguna diagonal inicializo a 1
        if indice_fila == colum or indice_fila == 4 - colum:
            fila.append(1)
            #No estoy en diagonal, inicializo a 0
        else:
            fila.append(0)
        matriz.append(fila)
    # Recorro para mostrar tabla
    for fila in matriz:
        for elemento in fila:
            print(elemento," ",end="")
        print()

tabla_bi(1)


marco = []
num_filas = 5
num_cols = 15
for indice_fila in range(0,num_filas):
    fila = []
    for indice_col in range(0,num_cols):
        if indice_fila == 0 or indice_fila == num_filas - 1 or indice_col == 0 or indice_col == num_cols -1:
            fila.append(1)
        else:
            fila.append(0)
    marco.append(fila)
for fila in marco:
    for elemento in fila:
        print(elemento," ",end="")
    print()




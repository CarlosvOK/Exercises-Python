lista = []
while True:
    print("\n")
    print("1. Añadir número a la lista")
    print("2. Añadir número de la lista en una posición")
    print("3. Longitud de la lista")
    print("4. Eliminar el último número")
    print("5. Eliminar un número")
    print("6. Contar números")
    print("7. Posiciones de un número")
    print("8. Mostrar números")
    print("9. Salir")
    opcion = int(input("Dime opción:"))
    if opcion == 1:
        num = int(input("Dime un número:"))
        lista.append(num)
    elif opcion == 2:
        num = int(input("Dime un número:"))
        pos = int(input("Dime una posición (empezando por 1):"))
        if pos > len(lista):
            print("Posición incorrecta")
        else:
            lista.insert(pos - 1,num)
    elif opcion == 3:
        print("Longitud de la lista: %d" % len(lista))
    elif opcion == 4:
        if len(lista)>0:
            print("El último elemento es %d y lo borramos." % lista.pop())
        else:
            print("La lista está vacía")
    elif opcion == 5:
        pos = int(input("Dime una posición (empezando por 1):"))
        if pos > len(lista):
            print("Posición incorrecta")
        else:
            print("El elemento es %d y lo borramos." % lista.pop(pos - 1))
    elif opcion == 6:
        num = int(input("Dime un número:"))
        print("El número %d aparece %d veces en la lista." % (num,lista.count(lista)))
    elif opcion == 7:
        num = int(input("Dime un número:"))
        indice_buscar = 0
        print("Posiciones: ",end="")
        for indice in range(0,lista.count(num)):
            indice_buscar = lista.index(num,indice_buscar)
            indice_buscar +=1
            print(indice_buscar," ",end="")
        print()
    elif opcion == 8:
        for num in lista:
            print(num," ",end="")
        print()
    elif opcion == 9:
        break
    else:
        print("Opción incorrecta")

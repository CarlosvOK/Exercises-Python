from bisect import bisect,insort

def ordenar (lista):
    lista_ordenada=[]

    for e in lista:
        posicion=bisect(lista_ordenada,e)
        insort(lista_ordenada,e)

    return lista_ordenada

numeros=[10,8,4,1,3,9,6,2,7,5]
print(numeros)


resultado=ordenar(numeros)
print(resultado)

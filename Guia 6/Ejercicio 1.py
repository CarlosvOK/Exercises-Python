import random

def listaAleatorios(n):
      lista_numeros = []
      for numeros in range(n):
          lista_numeros.append(random.randint(1,10))
          
      for numero in lista_numeros:
          print(numero," ",numero ** 2," ",numero ** 3)

      return listaAleatorios
n=0
n=int(input("Ingrese cuantos numeros aleatorios desea obtener: "))


aleatorios=listaAleatorios(n)


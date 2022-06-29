n= int(input("Introduzca número factoriales a calcular: "))

for i in range(1,n+1):
               n = int(input("Introduzca un número para calcular su factorial: "))
               factorial = 1

               for j in range(2,n+1):

                   factorial *= j

                   print(i,n,factorial)

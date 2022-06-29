def triangularIterativo(n):
    triangular = 0
    for i in range(1,n+1):
        triangular +=i
        return triangular

def triangularCalculado(n):
    return int(n * (n+1)/2)

n = int(input("Introduzca número de triangulares a calcular: "))

for i in range(1,n+1):
    print (i,"  -  ",triangularIterativo(i))

print()

for i in range(1,n+1):
    print (i,"  -  ",triangularCalculado(i))

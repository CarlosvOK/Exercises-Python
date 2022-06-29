n=int(input("Introduzca número máximo del dominó: "))

print("Introduzca solo valores numéricos enteros\n")
for i in range (n+1):
    for j in range (i,n+1):
        print(i,j)

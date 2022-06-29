inicial= int(input("Introduzca valor inicial: "))
final= int(input("Introduzca valor final: "))
if inicial % 2 == 1:

    inicial+=1
for i in range(inicial,final+1,2):
    print(i)

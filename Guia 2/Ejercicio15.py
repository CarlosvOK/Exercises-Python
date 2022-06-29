n = int(input("Ingrese un numero, el cual desea convertir: "))
numeros = [1000, 500, 100, 50, 10, 5, 1]
#sim=simbolos
sim = {1000:"M", 500:"D", 100:"C", 50:"L", 10:"X", 5:"V", 1:"I"}

rem= 0

for i in range(len(str(n)), 0, -1):
    #pos=posicion
    pos= i 
    num = (n-n%(10**(pos-1)))%(10**pos) 
    while(num>0):
        for div in numeros:

            if num/div == 1:
                print(sim[div], end="")
                num-=div
                break

            if num/div > 1:
                print(sim[div],end="")
                num-=div
                break

            if (num+(10**(pos-1)))/div == 1:
                print(sim[div-num], end="")
                print(sim[div], end="")
                num-=div
                break

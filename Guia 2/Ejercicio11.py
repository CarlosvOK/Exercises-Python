num=int(input("Ingresar un numero: "))

if num % 2 == 0:
    print(f"El número {num} es par.")

else:
    print(f"El número {num} es impar.")

numero= int(input("¿Qué número quieres saber si es primo?: "))
valor= range(2,numero)
contador = 0
for n in valor:
  if numero % n == 0:
    contador +=1
    print("divisor:", n)
 
if contador > 0 :
  print("El numero no es primo" )
else:
  print("El numero es primo")



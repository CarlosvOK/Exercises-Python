a = float( input('Introduce el primer valor: ') )
minimo = a
maximo = a
b = float( input('Introduce el segundo valor: ') )
if b < minimo:
 minimo = b
else:
 maximo = b
c = float( input('Introduce el tercer valor: ') )
if c < minimo:
 minimo = c
elif c < maximo:
 maximo = c

suma=a+b+c
promedio=suma/3
print("El maximo negativo es", minimo)
print("El minimo positivo es", maximo)
print(f"El promedio de los numeros ingresados es de: {promedio}")

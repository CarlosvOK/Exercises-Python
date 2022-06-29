#Datos que se pide al usuario ingresar
num1 = int(input("ingrese un número: "))
num2 = int(input("ingrese otro numero: "))

#Datos de salida. Hago un menu para decirle al usuario como debe elegir 
print("M E N U    D E   O P C I O N E S ")
print("1-Suma")
print("2-Resta")
print("3-Multiplicacion")
#Dato entrada
operacion = input( "¿Que operacion deseas realizar? Elija un numero: ")
#Formulas
if operacion == "1":
    print(num1 + num2)
elif operacion == "2":
    print(num1 - num2)
elif operacion == "3":
    print(num1 * num2)

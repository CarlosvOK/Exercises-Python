numero1 = int(input("ingrese un número: "));
numero2 = int(input("ingrese otro numero: "));
operacion = input( "Indique que operacion quiere: "  "suma, resta, division, multiplicacion: ");
 
if operacion == "suma":
    print(numero1 + numero2)
elif operacion == "resta":
    print(numero1 - numero2)
elif operacion == "division":
    print(numero1 / numero2)
elif operacion == "multiplicacion":
    print(numero1 * numero2)

print("T A B L A   D E  M U L T I P L I C A C I Ó N")

numero=int(input("Ingrese un numero: "))

for i in range(1,11):
    print(f"{i} x {numero} = {i * numero}")




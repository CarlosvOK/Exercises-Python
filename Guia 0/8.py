inversion=float(input("Introduzca la inversion inicial, por favor: "))
intereses=0.04
cant_ahorros1= inversion * (1 + intereses)
print("Ahorros tras el primer año: " + str (round(cant_ahorros1, 2)))
cant_ahorros2= cant_ahorros1 * (1 + intereses)
print("Ahorros tras el segundo año: " + str (round(cant_ahorros2, 2)))
cant_ahorros3= cant_ahorros2 * (1 + intereses)
print("Ahorros tras el tercer año: " + str (round(cant_ahorros3, 2)))

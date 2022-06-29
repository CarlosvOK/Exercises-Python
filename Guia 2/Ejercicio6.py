print("1-Ingrese la primer fecha")
#Datos de entrada
dia=int(input("Ingrese el dia: "))
mes=int(input("Ingrese el mes: "))
año=int(input("Ingrese el año: "))

print("2-Ingrese la segunda fecha")
#Datos de entrada
dia1=int(input("Ingrese el dia: "))
mes1=int(input("Ingrese el mes: "))
año1=int(input("Ingrese el año: "))
#Datos de salida
if año>año1:
    print(f"La primer fecha es la mas reciente: {dia}/{mes}/{año}")
#Si la primera condicion no se cumple entonces....
else:
    print(f"La segunda fecha es la mas reciente: {dia1}/{mes1}/{año1}")

nombres = []
edades = []
while True:
    nombre = input("Ingrese su nombre por favor: ")
    if nombre != "*":
        nombres.append(nombre)
        edades.append(int(input("Ingrese su edad: ")))
    if nombre == "*": break;	


edad_max = max(edades)
# Alumnos mayores de edad
print("Alumnos mayores de edad")
print("=======================")
for nombre,edad in zip(nombres,edades):
    if edad >= 18:
        print(nombre)
	
# Alumnos mayores 
print()
print("Alumnos mayores")
print("===============")
for nombre,edad in zip(nombres,edades):
    if edad == edad_max:
        print(nombre)

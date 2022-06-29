temperaturas = []
for indice in range(1,6):
    temperatura = []
    temperatura.append(int(input("Día %d. Temperatura máxima:" % indice)))
    temperatura.append(int(input("Día %d. Temperatura mínima:" % indice)))
    temperaturas.append(temperatura)


print("Temperaturas medias")
print("===================")

indice = 1
for temperatura in temperaturas:
    print("Día %d. Temperatura media: %f:" % (indice,sum(temperatura)/len(temperatura)))
    indice += 1


temp_min = temperaturas[0][1];
for temperatura in temperaturas:
    if temperatura[1] < temp_min:
        temp_min = temperatura[1]


print("Días con menos temperatura")
print("==========================")
indice = 1
for temperatura in temperaturas:
    if temperatura[1] == temp_min:
        print("Día %d" % indice)
        indice +=1
	

existe_temperatura = False
print("Días con temperatura máxima")
print("===========================")
temp_max = int(input("Introduce una temperatura:"))
indice = 1
for temperatura in temperaturas:
    if temperatura[0] == temp_max:
        print("Día %d" % indice)
        existe_temperatura = True
        indice +=1
if not existe_temperatura:
    print("No hay ningún día con dicha temperatura.")
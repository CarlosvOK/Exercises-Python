num_equipos = 15
equipos = []
resultados = []
#Muestro por pantalla cada nombre del equipo y los goles que hicieron por partido
for indice in range(0,num_equipos):
    partido = []
    partido.append(input("Introduce el nombre del equipo 1 del partido %d:" % (indice+1)))
    partido.append(input("Introduce el nombre del equipo 2 del partido %d:" % (indice+1)))
    equipos.append(partido)
    goles = []
    goles.append(int(input("Introduce los goles metidos por el equipo %s:" % (partido[0]))))
    goles.append(int(input("Introduce los goles metidos por el equipo %s:" % (partido[1]))))
    resultados.append(goles)

print("QUINIELA")
print("========")

for partido,goles in zip(equipos,resultados):
    print(partido[0],"-",partido[1],":",end="")
    if goles[0] > goles[1]:
        print("-> 1")
    else:
        if goles[0] < goles[1]:
            print("-> 2")
        else:
            print("-> X")

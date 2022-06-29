print("Bienvenidxo al control de partidos")
continuar="SI"
punto=int
while continuar=="SI":
    equipo=int(input("Ingrese el numero de su equipo: "))
    resultado=input("¿Como le fue como el resultado [P= Perdido, E= Empatado, G= Ganado]: ")

    if resultado=="P":
        punto=(0)
        print("Lamentablemente no gano puntos")

    elif resultado=="E":
        punto=(1)
        print("Bien!! Usted gano 1 punto")
        

    elif resultado=="G":
        punto=(3)
        print("¡Genial! Usted gano 3 puntos ¡olé!")

    if punto<=0:
        print(f"Ups usted Equipo {equipo} hizo la menor cantidad de puntos")


    print (f"Su equipo es:{equipo}")
    print(f"Usted gano un total de: {punto}")

    
        
    
    continuar=input("Desea continuar SI/NO: ")

    print("¡Hasta El Proximo Evento!")




    




    
       
  

peso=float(0.0)
estatura=float(0.0)
imc=float(0.00)

peso=input("Ingrese su peso, en Kilogramos: ")
    
estatura=input("Ingrese su altura, en Metros: ")
    
imc=round((float(peso)/float(estatura)),int(2))
print("Tu Índice de masa corporal es de: " + str(imc))

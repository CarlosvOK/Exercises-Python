def nuevafecha(fecha,num):
    return nuevafecha

fecha_dia=-1
fecha_mes=-1
while fecha_dia<0 or fecha_dia>31:
    fecha_dia=int(input("Introduce El Dia: "))
    if fecha_dia<0:
        print("Error, Ingrese Un Valor Positivo")
    if fecha_dia>31:
        print("Error,Ingrese Un Valor Entre El 1-31")
        
while fecha_mes<0 or fecha_mes>12:
    fecha_mes=int(input("Introduce El Mes: "))
    if fecha_mes<0:
        print("Error, Ingrese Un Valor Positivo")
    if fecha_mes>12:
        print("Error,Ingrese Un Valor Entre El 1-12")
        
fecha_año= int(input("Introduce El Año: "))

num=int(input("Introduce Un Numero: "))

fecha_nueva=fecha_dia+num
fecha_nueva0=fecha_mes+num
fecha_nueva1=fecha_año+num

print(f"Año-{fecha_nueva1}-Mes-{fecha_nueva0}-Dia-{fecha_nueva}")



    
    

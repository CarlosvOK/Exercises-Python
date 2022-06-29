##DECLARACIONES DE VARIABLES:
def horas_dias(hora,minuto,segundo,hora1,minuto1,segundo1):
    segundo=-1
    segundo1=-1
    hora_total=0
    minuto_total=0
    segundo_total=0
    
    hora=int(input("Ingrese La Hora: "))
    minuto=int(input("Ingrese El Minuto: "))

    while segundo<0 or segundo>60:
        segundo=int(input("Ingrese El Segundo: "))
        if segundo<0:
            print("Error,Ingrese un numero positivo")
        if segundo>60:
            print("Error, Ingres eun valor valido Hasta 60")
    print()
    print("TIEMPO PARA SUMAR")
    print()

    hora1=int(input("Ingrese La Hora: "))
    minuto1=int(input("Ingrese El Minuto: "))

    while segundo1<0 or segundo1>60:
        segundo1=int(input("Ingrese El Segundo: "))
        if segundo1<0:
            print("Error,Ingrese un numero positivo")

        if segundo1>60:
            print("Error, Ingres eun valor valido Hasta 60")


    hora_total=hora+hora1
    minuto_total=minuto+minuto1
    segundo_total=segundo+segundo1

    print(f"{hora_total}H-{minuto_total}M-{segundo_total}S")

   
horas_dias(1,2,3,1,2,3)






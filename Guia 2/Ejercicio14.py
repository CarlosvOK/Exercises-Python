Dia=["Lunes", "Martes", "Miercoles", "Jueves", "viernes", "Sabado", "Domingo"]

numero= int(input("Ingresar el numero del dia del año: "))

if (numero > 0 and numero <366):

    if (numero <=7):
        print(str(Dia[numero-1]))

    elif ((numero%7)==0):
        print(str(Dia[6]))

    else:
        print(str(Dia[(numero-1)%7]))

else:
    numero=print("Ingrese un numero entre el 1 y 365")

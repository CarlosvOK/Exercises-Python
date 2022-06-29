def cant_dias(mes):
    if mes.lower() in ("enero",",marzo","julio,","agosto","octubre","diciembre"):
        return "31"
    elif mes.lower()=="febrero":
        return "28/29"
    else:
        return "30"


nombre_mes= input("Ingrese el nombre del mes, por favor: ")
año=int(input("Ingrese el año: "))
print(cant_dias(nombre_mes))


año=int(input("Ingrese el año: "))
mes=input("Ingrese el mes: ")
dia=input("Ingrese el dia: ")

dia=dia.zfill(2)

mes=mes.zfill(2)
    
print(f"{dia}/{mes}/{año%100}")



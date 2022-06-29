def fraccion(numerador,denominador):
    if(numerador < denominador):
        return fraccion (denominador, numerador);
    elif(denominador ==0):
        return numerador;
    else:
        return fraccion(denominador, int(numerador%denominador))

nf=int(input("Escriba el numerador: " ))
df=int(input("Escriba el denominador: " ))

numerador=(nf)*2
denominador=(df)*2

div=(fraccion(numerador,denominador))
print(f"La mayor cantidad de simplificaciones entre {nf}/{df} es: {numerador/div}/{denominador/div}")

promedio=0
contador=0
contador_igual=0
contador_negativo=1
while True:
    while True:
        contador+=1
        x=int(input('Ingresar primer numero'))
        y=int(input('Ingresar segundo numero'))
        if x==y:
            print('ERROR Los numeros no deben ser iguales')
            contador_igual+=1
        elif x<0 or y<0:
            print('Los numero no deben ser negativos')
            contador_negativo+=1
        else:
            break
    salir=input('Para salir, digite si')
    if salir=='si' or salir=='Si':
        break
print('Las veces que se a ejecutado el codigo es:',contador)
print('Las veces que digitaron numeros iguales es:',contador_igual)
print('Las veces que se digitaron numeros negatvos es:',contador_negativo)
promedio=contador_igual/contador_negativo
print('El promedio es:',promedio)
    
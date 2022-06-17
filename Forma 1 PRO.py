N=100
suma_interna=0
cont1=0
cont2=0
suma1=0
while True:
    num1=int(input("Ingrese el primer intervalo: "))
    num2=int(input("Ingrese el segundo intervalo: "))
    if num1==num2:
        print("error los numeros son iguales")
    else:
        break
if num1>num2:
    minimo=num2
    maximo=num1
else:
    minimo=num1
    maximo=num2
while N!=0: #Indica que mientras que N sea diferente de 0 el bucle seguira
    N=int(input("ingrese un número ")) #Define el numero ingresado por el usuario 
    if N>minimo and N<maximo:
        suma_interna+=N
    elif N<minimo or N>maximo:
        suma1+=N
        cont1+=1
    elif N==minimo or N==maximo:
        cont2+=1
print("la suma de los numeros que estan dentro es:",suma_interna)
print("el promedio de los numeros fuera del intervalo es: ",suma1/cont1)
print("la cantidad de los numeros  ingresados iguales a los limites: ",cont2)
print("fin del programa ")


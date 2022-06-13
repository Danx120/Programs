#VARIABLES
num=1 #Variable que sirve para definir los numeros ingresados por el usuario
sumD=0 #Acumulador para guardar los numeros que estan dentro del intervalo
contF=-1 #Contador de las veces que se ha ingresado un numero que esta fuera del intervalo
contI=0 #Contador de las veces que el numero ingresado ha sido igual a los limites del intervalo
sumF=0 #Acumulador que guarda la suma de los numeros que estan fuera del intervalo

print ("___INTERVALOS___")
#1 FORMA
#Toma de datos ingresados por el usuario(Limites)
while True:
    Lim1=int(input("Ingrese el primer Limite del intervalo:   "))
    Lim2=int(input("Ingrese el segundo Limte del intervalo:   "))
#validacion para que los limites no sean iguales
    if Lim1==Lim2: 
        print("Los Limites del intervalo NO deben ser IGUALES")
        print("Vuelve a intentarlo....")
    else:
        break
#Valifacion para establecer el Limite maximo y minimo
if Lim1>Lim2:
    maximo=Lim1
    minimo=Lim2
else:
    maximo=Lim2
    minimo=Lim1

#Toma de datos(numeros) ingresados por el usuario y calculos
while num!=0:
    num=int(input("Ingrese un número(Ingrese 0 si desea salir):   "))
    if num<minimo or num>maximo:
        sumF += num
        contF += 1
    elif num>minimo and num<maximo: 
        sumD += num
    elif num==minimo or num==maximo:
        contI += 1
#Impresion en la pantalla de los resultados obtenidos
if contF>=1:
    print("la suma de los numeros que estan dentro es:",sumD)
    print("el promedio de los numeros fuera del intervalo es: ",sumF/contF)
    print("la cantidad de los numeros  ingresados iguales a los limites: ",contI)
else:    
    print("la suma de los numeros que estan dentro es:",sumD)
    print("la cantidad de los numeros  ingresados iguales a los limites: ",contI)
    print("No se ingreso ningun numero que este fuera del intervalo")




print("___FIN___")
#VARIABLES
num=1 #Variable que sirve para definir los numeros ingresados por el usuario
sumD=0 #Acumulador para guardar los numeros que estan dentro del intervalo
contF=0 #Contador de las veces que se ha ingresado un numero que esta fuera del intervalo
contI=0 #Contador de las veces que el numero ingresado ha sido igual a los limites del intervalo
sumF=0 #Acumulador que guarda la suma de los numeros que estan fuera del intervalo

print ("___INTERVALOS___")
#2 FORMA
#Toma de datos ingresados por el usuario(Limites)
while True:
    Lim1=int(input("Ingrese el primer Limite del intervalo: ")) 
    Lim2=int(input("Ingrese el segundo Limite del intervalo: "))
#Validacion para que los limites no sean iguales
    if Lim1==Lim2: 
        print("Los Limites NO deben ser IGUALES")
        print("Intentelo de nuevo.....")
    else:
        break 
#Validacion para establecer Limite maximo y Limite minimo
if Lim1>Lim2: 
    maximo=Lim1
    minimo=Lim2 
else: 
    maximo=Lim2
    minimo=Lim1
#Toma de datos(numero) ingresado por el usario y calculos
while True:
    num=int(input("ingrese un numero(Ingrese 0 si desea salir)  ")) 
    if num==0: 
        break
    else:
        print("puede continuar") 
    if num>minimo and num<maximo:
        sumD += num  
    elif num<minimo or num>maximo:
        sumF += num 
        contF += 1 
    elif num==minimo or num==maximo:
        contI += 1
#Impresion en pantalla de la informacion obtenida
print("la suma de los numeros que estan dentro es:",sumD)
print("el promedio de los numeros fuera del intervalo es: ",sumF/contF)
print("la cantidad de los numeros  ingresados iguales a los limites: ",contI)

print("___FIN___") 

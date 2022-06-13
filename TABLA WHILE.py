#TABLAS DE MULTIPLICAR

#FORMA While

#Variables
numpar = 0  #almacena la cantidad de numeros pares
numimpar = 0  #Almacena la cantidad de numeros impares
mul3 = 0 #Almacena la cantidad de numeros que son multiplos de 3
mul5 = 0 #Almacena la cantidad de numeros que son multiplos de 5
suma = 0 #Almacena la suma de los resultados de las tablas
cont1 = 1 #contador para el bucle de el numero de tablas que quiere que imprima el usuario
cont2 = 1 #contador para para el numero de multiplicaciones que quiere que haga el usuario


print ("TABLAS DE MULTIPLICAR")
print("")


#TOMA DE DATOS

while True:
    Tab=int(input("Ingrese hasta que tabla desea contar: "))  
    Num=int(input("Ingrese hasta que número quiere multiplicar: "))
#Validacion para que el numero ingresado por el usuario este dentro del intervalo de 2 a 100
    if Tab<2 or Tab>100: 
        print("El numero NO DEBE SER MENOR QUE 2 O MAYOR QUE 100")
#Validacion para que el numero ingresador por el usuario no sea negativo  
    if Tab<0: 
        print ("El numero NO debe ser NEGATIVO")
    else: 
       break #Cierre del bucle

#BUCLES Y CALCULO DE DATOS

while cont1<=Tab: #Bucle que controla el numero de tablas que se van a imprimir
    numpar = 0 #Definimos otra vez las variables en cero para evitar errores de calculo
    numimpar = 0 
    mul3 = 0 
    mul5 = 0 
    suma = 0
   
    print("La tabla del ",cont1," es:")
    
    while cont2<=Num: #Bucle que controla la cantidad de numeros que quiere multiplcar en la tablas

#Calulo de numeros impares, pares y multiplos de 3 y 5
        Rpt = cont1*cont2
        print(cont1,"*",cont2,"=", Rpt)
        if Rpt % 3 == 0:
            mul3 += 1
        
        if Rpt % 5 == 0:
            mul5 += 1
        if Rpt % 2 == 0:
            numpar += 1
        else:
            numimpar += 1
        suma += Rpt 
        cont2 += 1 #Contador que controla el bucle de los numeros multiplicados
    cont1 += 1 #Contador que va a controlar el bucle de las tablas
    cont2 -= Num #Contador que controla el bucle de los numeros multiplicados
        
#Impresion de datos obtenidos a partir de los bucles    
    print("La suma de la tabla del",Tab,"es:",suma)
    print("El promedio es:",suma/Num)
    print("Los multiplos de 3 son:",mul3)
    print("Los multiplos de 5 son:",mul5)
    print("Hay",numpar,"numeros pares")
    print("Hay",numimpar,"números impares")
    print("")

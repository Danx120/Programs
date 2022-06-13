#TABLAS DE MULTIPLICAR

#FORMA for

#Variables
numpar = 0 #almacena la cantidad de numeros pares
numimpar = 0 #Almacena la cantidad de numeros impares
mul3 = 0 #Almacena la cantidad de numeros que son multiplos del 3
mul5 = 0 #Almacena la cantidad de numeros que son multiplos del 5
suma = 0 #Almacena las respuestas de las tablas de multiplicar

#Toma de datos ingresados por el usuario
print ("TABLAS DE MULTIPLICAR")
print("")

while True:
    Tab=int(input("Ingrese hasta que tabla desea contar: "))  
    Num=int(input("Ingrese hasta que número quiere multiplicar: "))
    if Tab<2 or Tab>100: #Validacion para que el numero de tablas ingresado este dentro del intervalo de 2 a 100
        print("El numero NO DEBE SER MENOR QUE 2 O MAYOR QUE 100")
    if Tab<0: #Validacion para que el numero ingresado no sea negativo
        print ("El numero NO debe ser NEGATIVO")
    else: 
       break

for T in range(1,Tab+1): #Definimos un bucle para T desde 1 hasta el numero ingresado mas 1
      
#Enceramos todas las variables para evitar errores de calculo
      mul3 = 0 
      mul5 = 0
      numpar = 0
      numimpar = 0
      suma=0
      
      
      print("La tabla del ",T," es:")
      for N in range(1,Num+1): #Definimos el segundo bucle que se va a encargar de el segundo valor ingresado por el usuario
#Calculos y validaciones para contar numeros pares, impares, y los multiplos de 3 y de 5          
          Rpt = T*N
          suma += Rpt
          
          if Rpt % 3 == 0:
              mul3 += 1
          
          if Rpt % 5 == 0:
              mul5 += 1
          if Rpt % 2 == 0:
              numpar += 1
          else:
              numimpar += 1 
          print(T,"*",N,"=", Rpt) #Impresion de la tabla 

#Impresion de los datos obtenidos de cada una de las tablas que se van contando           
      print("La suma de la tabla del",T,"es:",suma)
      print("El promedio es:",suma/Num)
      print("Los multiplos de 3 son:",mul3)
      print("Los multiplos de 5 son:",mul5)
      print("Hay",numpar,"numeros pares")
      print("Hay",numimpar,"números pares")
      print("")
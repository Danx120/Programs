#En el ejercicio se nos pide que la impresion de los datos tenga un retraso de un segundo
#con lo cual necesitamos importar el modulo time
import time
#Pedimos al usuario que ingrese la dimension que va a tener el vector
dim=int(input('Ingrese la dimension que desea que tenga el vector: '))

#Creamos un vector(lista) con el tamaño que nos indico el usuario
M = [0] * dim

#Bucle for para que el usuario ingrese los numeros que iran dentro del vector
for i in range(dim):
    while True: #Bucle while que sirve para validar que los numeros ingresados por el usuario esten en el rango de 50 a 100
        num=int(input('Ingrese un numero:  '))
        if num < 50:
            print('El numero debe ser mayor que 50')
           
        elif num > 100:
            print('El numero debe ser menor que 100')
        
        else:
            break
    
    M[i] = num
    
print()
#Impresion del vector con los datos ingresados por el usuario
for i in range(dim):
    time.sleep(1)#Usamos el modulo time para crear un retraso de un segundo en la impresion
    print('El valor en la posicion',i,'es',M[i])

#ORDENAMIENTO BURBUJA
for j in range(len(M)-1): #Bucle for que sirve para recorrer el vector hasta que este ordenado

    for i in range(len(M)-1): #Bucle for que sirve para analizar cada valor del vector
        
        if M[i] > M[i + 1]: #Evaluacion: Si el numero analizado es mayor que el siguiente hacer
            AUX = M[i] #Creamos una variable que almacenara el valor analizado
            M[i] = M[i + 1] #Cambiamos el valor por el valor siguiente
            M[i + 1] = AUX #Almacenamos el valor siguiente en la variable creada
#Esto hara que los numeros que se vayan analizando roten de posicion, el bucle seguira hasta que no haya ningun valor mayor al valor siguiente
print()

#Impresion de datos ya ordenados
for i in range(dim):
    time.sleep(1) #Igualmente usamos el modulo time para generar un retraso en la impresion de los datos 
    print('El vector ordenado en la posicion',i,'es',M[i])      



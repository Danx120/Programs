
while True:
    dim = int(input('Ingrese la dimension que desea que tenga el vector: '))
    if dim<5:
        print ('La dimension debe ser mayor que 5')
    elif dim>30:
        print('La dimension debe ser menor que 30')
    else:
        break

N=[0]*dim
M=[0]*dim
S=[0]*dim
R=[0]*dim
MU=[0]*dim
D=[0]*dim

for i in range(dim):
    num=int(input('Ingrese un numero para el vector 1:  '))
    N[i]=num


for i in range(dim):
    num=int(input('Ingrese un numero para el vector 2:  '))
    M[i]=num
print()

print('Los valores almacenados en el vector 1 son:',N)
print('Los valores almacenados en el vector 2 son:',M)





print()


for i in range(dim):
            S[i]=N[i]+M[i]
         
    
    
for i in range(dim):
            R[i]=N[i]-M[i]
       
    

for i in range(dim):
         MU[i]=N[i]*M[i]
       
    
    
for i in range(dim):
            D[i]=N[i]/M[i]
            

while True:
    respuesta=str(input('Que operacion desea hacer?(Digite Salir para terminar) '))
    
    if respuesta=='suma':
            print("La suma es:",S)
            
    elif respuesta=='resta':
            print("La resta es:",R)
            
    elif respuesta=='multiplicacion':
            print("La multiplicacion es:",MU)
            
    elif respuesta=='division':
            print('La division es:',D)
            
    elif respuesta=='Salir':
        break
    
#Ing buenas tardes solo me faltaba una linea de codigo, por eso le entrego este ejercicio fuera de tiempo.
#El ejercicio esta terminado y corre correctamente
#Si me puede ayudar haciendo valido este ejercicio ya que el otro estaba a punto de terminar pero se me acabo el tiempo
#Muchas gracias ing :)


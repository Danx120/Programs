
#Definicion de la funcion isPrime con el argumento de Num
def isPrime(Num):
    M = 0#Contador para los numeros primos
    for i in range(1,Num+1):
        if Num % i == 0: #Validacion de los numeros primos(si el resto es 0, es un numero primo)
            M += 1 #Contador de las divisiones que se realizan en el numero
    if M == 2: #Validacion (si el contador es igual que dos, es decir la division del numero dio como resultado cero en dos ocasiones)
       return True #ES PRIMO
    else : #Si la division dio como resultado 0 mas o menos veces, entonces no es primo
        return False#NO ES PRIMO
#El numero es primo si el resto de la division da cero, pero solo en dos ocasiones:
#1-cuando es divisible para si mismo
#2-cuando es divisible para uno

for i in range(1,20): #Definimos el rango hasta el cual nos va a imprimir los resultados(En el archivo especifica que es 20)
     if isPrime(i+1):#Validacion para los numeros que son primos dentro del rango
         print(i+1,end=" ")#Impresion del numero primo
         
print()#Espacio
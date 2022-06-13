#variables
numf = 0
sumi = 0
numi = 0
numo = 0
numt = 0

#solicitud de datos


limSuperior = int(input("Ingresa el numero para iniciar el intervalo: "))
limInferior = int(input("Ingresa otro numero para cerrar el intervalo:  "))

while limSuperior == limInferior:
    print ("Los limites del intervalo no deben ser iguales")
    print("limite invalido vuelve a intentarlo....")
    limSuperior = int(input("Ingrese correctamente el primer limite del intervalo:"))
    limInferior = int(input("Ingrese correctamente el segundo limite del intervalo:"))
    


while limSuperior > limInferior:
        print("El límite inferior no puede ser mayor al superior.")
        print("limite invalido vuelve a intentarlo....")
        limSuperior = int(input("Ingrese correctamente el primer limite del intervalo:"))
        limInferior = int(input("Ingrese correctamente el segundo limite del intervalo:"))
           
    
num = int(input("\nIntroduce un número (Ingresa 0, para salir): "))

while num!=0:
        if num>limSuperior and num<limInferior: 
            sumi += num
        else:  
            numf += 1
            numo += num
            if num==limSuperior or num==limInferior:
                numi += 1
        num = int(input("Introduce un número (Ingresa 0, para salir): "))
        numt += 1 
       
numt = numf/numt 
numo = numo/numf       
       
#Informacion recolectada
print("informacion obtenida :")
print("La suma de los números dentro del intervalo es",sumi)
print("La cantidad de numeros que estan fuera del intervalo es:",numf)
print("La cantidad de numeros que fueron iguales a los limites del intervalo es:",numi)
print("El promedio de numeros ingresados que estan fuera del intervalo es:",numt)
print("El promedio de los numeros que estan fuera del intervalo es:",numo)
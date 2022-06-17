#Funcion de litros cada 100km
def l100kmtompg(litros):
    Mi=(100*1000)/1609.344 #Transformacion de km a millas
    Gal= litros/3.785411784 #Transformacion de litros a galones
    return Mi/Gal #Return de los datos en forma de Millas sobre Galon

#Impresion de resultados con los valores de prueba 
print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10.))
    
    
 #Funcion de millas por galon  
def mpgtol100km(millas):
    lit=3.785411784 #definicion de cuanto equivale un galon en litros 
    Kil=(millas*1609.344)/1000 #Transformacion de millas a kilometros
    Km=Kil/100 
    return lit/Km#Return de los valores en fomra de litros sobre kilometros

#Impresion de resultados con los valores de prueba
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))


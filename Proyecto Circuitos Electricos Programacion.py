
import time
import numpy as np
import turtle
import random

#Resisitivo--------------------------------------------------
Serie = []
Paralelo = []
Voltaje = []
Corriente = []

circuito = turtle.Turtle()



def esquema_del_circuito(Serie,Paralelo,Voltaje,Corriente):
    for x in range(len(Serie)):
        circuito.pencolor('blue')
        circuito.forward(25)
        circuito.left(70)
        circuito.forward(25)
        circuito.right(135)
        circuito.forward(50)
        circuito.left(135)
        circuito.forward(25)
        circuito.right(70)
        circuito.forward(25)
    if len(Paralelo) > 0:
        for y in range(len(Paralelo)):
            circuito.pencolor('purple')
            circuito.right(90)
            circuito.forward(25)
            circuito.right(70)
            circuito.forward(25)
            circuito.left(150)
            circuito.forward(50)
            circuito.right(150)
            circuito.forward(25)
            circuito.left(70)
            circuito.forward(25)
            circuito.left(180)
            circuito.up()
            circuito.forward(75)
            circuito.right(90)
            circuito.down()
            circuito.forward(90)
                
        circuito.up()
        circuito.left(90)
        circuito.forward(15)
        circuito.right(180)
        circuito.down()
        circuito.forward(30)
        circuito.up()
        circuito.left(180)
        circuito.forward(15)
        circuito.right(90)
        circuito.forward(10)
        circuito.left(90)
        circuito.forward(7)
        circuito.right(180)
        circuito.down()
        circuito.forward(14)
        circuito.up()
        circuito.forward(67)
        circuito.right(90)
        circuito.forward(100)
        circuito.down()
        circuito.goto(0,-75)
    elif len(Paralelo) == 0:
        circuito.up()
        circuito.left(90)
        circuito.forward(15)
        circuito.right(180)
        circuito.down()
        circuito.forward(30)
        circuito.up()
        circuito.left(180)
        circuito.forward(15)
        circuito.right(90)
        circuito.forward(10)
        circuito.left(90)
        circuito.forward(7)
        circuito.right(180)
        circuito.down()
        circuito.forward(14)
        circuito.up()
        circuito.right(180)
        circuito.forward(7)
        circuito.left(90)
        circuito.forward(20)
        circuito.left(90)
        circuito.down()
        circuito.forward(75)
        circuito.right(90)
        circuito.goto(0,-72)
        
    
    circuito.down()
    circuito.forward(25)
    
    for i in range(len(Voltaje)):
        circuito.pencolor('brown')
        circuito.right(90)
        circuito.circle(35)

        circuito.up()
        circuito.left(90)

        circuito.forward(10)
        circuito.down()
        circuito.forward(15)
        circuito.right(135)
        circuito.up()
        circuito.forward(10)
        circuito.right(135)
        circuito.down()
        circuito.forward(15)
        circuito.up()
        circuito.right(90)
        circuito.forward(30)
        circuito.right(90)
        circuito.forward(7)
        circuito.left(90)
        circuito.down()
        circuito.forward(10)
        circuito.up()
        circuito.forward(10)
        circuito.down()
        circuito.forward(25)
        
    for i in range(len(Corriente)):
        circuito.pencolor('black')
        circuito.right(90)
        circuito.circle(35)

        circuito.up()
        circuito.left(90)

        circuito.forward(10)
        circuito.down()
        circuito.forward(40)
        circuito.left(135)
        circuito.forward(10)
        circuito.left(135)
        circuito.forward(15)
        circuito.left(135)
        circuito.forward(10)
        circuito.up()
        circuito.right(45)
        circuito.forward(20)
        circuito.down()
        circuito.forward(25)
    
    circuito.right(90)
    circuito.forward(75)
    circuito.right(90)
    circuito.goto(0,0)

def esquema_Inductivo(Serie,Paralelo,Voltaje,Corriente):

    
    for i in range(len(Serie)):
        circuito.pencolor('purple')
        circuito.forward(15)
        circuito.left(70)
        circuito.forward(15)
        circuito.right(140)
        circuito.forward(35)
        circuito.right(110)
        circuito.forward(15)
        circuito.right(115)
        circuito.forward(40)
        circuito.right(125)
        circuito.forward(40)
        circuito.right(120)
        circuito.forward(15)
        circuito.right(115)
        circuito.forward(40)
        circuito.right(130)
        circuito.forward(40)
        circuito.right(115)
        circuito.forward(15)
        circuito.right(130)
        circuito.forward(25)
        circuito.right(50)
        circuito.forward(15)
    if len(Paralelo) > 0:
        for i in range(len(Paralelo)):
            circuito.pencolor('green')
            circuito.right(90)
            circuito.forward(25)
            circuito.right(70)
            circuito.forward(20)
            circuito.left(150)
            circuito.forward(40)
            circuito.left(100)
            circuito.forward(20)
            circuito.left(125)
            circuito.forward(50)
            circuito.left(130)
            circuito.forward(50)
            circuito.left(100)
            circuito.forward(20)
            circuito.left(125)
            circuito.forward(50)
            circuito.left(130)
            circuito.forward(50)
            circuito.left(110)
            circuito.forward(20)
            circuito.left(130)
            circuito.forward(45)
            circuito.left(50)
            circuito.forward(25)
            circuito.up()
            circuito.left(180)
            circuito.forward(115)
            circuito.right(90)
            circuito.down()
            circuito.forward(100)
        circuito.up()
        circuito.left(90)
        circuito.forward(15)
        circuito.right(180)
        circuito.down()
        circuito.forward(30)
        circuito.up()
        circuito.left(180)
        circuito.forward(15)
        circuito.right(90)
        circuito.forward(10)
        circuito.left(90)
        circuito.forward(7)
        circuito.right(180)
        circuito.down()
        circuito.forward(14)
        circuito.up()
        circuito.forward(105)
        circuito.right(90)
        circuito.forward(110)
        circuito.down()
        circuito.goto(0,-115)
    elif len(Paralelo) == 0:
        circuito.up()
        circuito.left(90)
        circuito.forward(15)
        circuito.right(180)
        circuito.down()
        circuito.forward(30)
        circuito.up()
        circuito.left(180)
        circuito.forward(15)
        circuito.right(90)
        circuito.forward(10)
        circuito.left(90)
        circuito.forward(7)
        circuito.right(180)
        circuito.down()
        circuito.forward(14)
        circuito.up()
        circuito.right(180)
        circuito.forward(7)
        circuito.left(90)
        circuito.forward(20)
        circuito.left(90)
        circuito.down()
        circuito.forward(75)
        circuito.right(90)
        circuito.goto(0,-72)
        
    circuito.down()
    circuito.forward(25)
    
    for i in range(len(Voltaje)):
        circuito.pencolor('brown')
        circuito.right(90)
        circuito.circle(35)

        circuito.up()
        circuito.left(90)

        circuito.forward(10)
        circuito.down()
        circuito.forward(15)
        circuito.right(135)
        circuito.up()
        circuito.forward(10)
        circuito.right(135)
        circuito.down()
        circuito.forward(15)
        circuito.up()
        circuito.right(90)
        circuito.forward(30)
        circuito.right(90)
        circuito.forward(7)
        circuito.left(90)
        circuito.down()
        circuito.forward(10)
        circuito.up()
        circuito.forward(10)
        circuito.down()
        circuito.forward(25)
        
    for i in range(len(Corriente)):
        circuito.pencolor('black')
        circuito.right(90)
        circuito.circle(35)

        circuito.up()
        circuito.left(90)

        circuito.forward(10)
        circuito.down()
        circuito.forward(40)
        circuito.left(135)
        circuito.forward(10)
        circuito.left(135)
        circuito.forward(15)
        circuito.left(135)
        circuito.forward(10)
        circuito.up()
        circuito.right(45)
        circuito.forward(20)
        circuito.down()
        circuito.forward(25)
    
    circuito.right(90)
    circuito.forward(100)
    circuito.right(90)
    circuito.goto(0,0)

def esquema_capacitivo(Serie,Paralelo,Voltaje,Corriente):
    for i in range(len(Serie)):
        circuito.pencolor('purple')
        circuito.forward(20)
        circuito.up()
        circuito.left(90)
        circuito.forward(25)
        circuito.right(180)
        circuito.down()
        circuito.forward(50)
        circuito.up()
        circuito.left(180)
        circuito.forward(25)
        circuito.right(90)
        circuito.forward(15)
        circuito.left(90)
        circuito.forward(25)
        circuito.right(180)
        circuito.down()
        circuito.forward(50)
        circuito.up()
        circuito.left(180)
        circuito.forward(25)
        circuito.right(90)
        circuito.down()
        circuito.forward(20)
    if len(Paralelo) > 0:
        for x in range(len(Paralelo)):
            circuito.pencolor('green')
            circuito.right(90)
            circuito.forward(30)
            circuito.up()
            circuito.right(90)
            circuito.forward(25)
            circuito.left(180)
            circuito.down()
            circuito.forward(50)
            circuito.up()
            circuito.right(180)
            circuito.forward(25)
            circuito.left(90)
            circuito.forward(15)
            circuito.right(90)
            circuito.forward(25)
            circuito.left(180)
            circuito.down()
            circuito.forward(50)
            circuito.up()
            circuito.right(180)
            circuito.forward(25)
            circuito.left(90)
            circuito.down()
            circuito.forward(30)
            circuito.up()
            circuito.left(180)
            circuito.forward(75)
            circuito.right(90)
            circuito.down()
            circuito.forward(75)
        circuito.up()
        circuito.left(90)
        circuito.forward(15)
        circuito.right(180)
        circuito.down()
        circuito.forward(30)
        circuito.up()
        circuito.left(180)
        circuito.forward(15)
        circuito.right(90)
        circuito.forward(10)
        circuito.left(90)
        circuito.forward(7)
        circuito.right(180)
        circuito.down()
        circuito.forward(14)
        circuito.up()
        circuito.forward(68)
        circuito.right(90)
        circuito.forward(85)
        circuito.down()
        circuito.goto(0,-75)
    elif len(Paralelo) == 0:
    
        circuito.up()
        circuito.left(90)
        circuito.forward(15)
        circuito.right(180)
        circuito.down()
        circuito.forward(30)
        circuito.up()
        circuito.left(180)
        circuito.forward(15)
        circuito.right(90)
        circuito.forward(10)
        circuito.left(90)
        circuito.forward(7)
        circuito.right(180)
        circuito.down()
        circuito.forward(14)
        circuito.up()
        circuito.right(180)
        circuito.forward(7)
        circuito.left(90)
        circuito.forward(20)
        circuito.left(90)
        circuito.down()
        circuito.forward(75)
        circuito.right(90)
        
    circuito.down()
    circuito.forward(25)
    for i in range(len(Voltaje)):
        circuito.pencolor('brown')
        circuito.right(90)
        circuito.circle(35)

        circuito.up()
        circuito.left(90)

        circuito.forward(10)
        circuito.down()
        circuito.forward(15)
        circuito.right(135)
        circuito.up()
        circuito.forward(10)
        circuito.right(135)
        circuito.down()
        circuito.forward(15)
        circuito.up()
        circuito.right(90)
        circuito.forward(30)
        circuito.right(90)
        circuito.forward(7)
        circuito.left(90)
        circuito.down()
        circuito.forward(10)
        circuito.up()
        circuito.forward(10)
        circuito.down()
        circuito.forward(25)
        
    for i in range(len(Corriente)):
        circuito.pencolor('black')
        circuito.right(90)
        circuito.circle(35)

        circuito.up()
        circuito.left(90)

        circuito.forward(10)
        circuito.down()
        circuito.forward(40)
        circuito.left(135)
        circuito.forward(10)
        circuito.left(135)
        circuito.forward(15)
        circuito.left(135)
        circuito.forward(10)
        circuito.up()
        circuito.right(45)
        circuito.forward(20)
        circuito.down()
        circuito.forward(25)
    
    circuito.right(90)
    circuito.forward(75)
    circuito.right(90)
    circuito.goto(0,0)


        

def Validacion1(A):
    if A != 'R' and A != 'I' and A != 'C':
        print('El caracter ingresado es incorrecto')
        return A
    else:
        return A
    
def TipoDeCir(A):
    if A == 'R':
        R = 'R'
        return R
    elif A == 'I':
        I = 'I'
        return I
    elif A == 'C':
        C = 'C'
        return C


def fuentesV(Fv,Voltaje):
   
    if Fv =='S':
        TotalV = sum(Voltaje)
        return TotalV 
    elif Fv == 'P':
        suma = sum(Voltaje)
        mult = np.prod(Voltaje)
        TotalV = mult/suma
        return TotalV 
            
def fuentesC(Fc,Corriente):
   
    if Fc =='S':
        TotalC = sum(Corriente)
        return TotalC 
    elif Fc == 'P':
        suma = sum(Corriente)
        mult = np.prod(Corriente)
        TotalC = mult/suma
        return TotalC 
                
    
print()
time.sleep(1)
print('BIENVENIDO')
print()
time.sleep(1)
print('Resolucion de circuitos electricos')
print()
time.sleep(2)
print('Circuitos Resisitivos(R); Circuitos Inductivos(I); Circutos Capacitivos(C)')
print('\n')
print()

while True:
    print('\n')
    A = str(input('Seleccione el tipo de circuito que desea armar: '))
    Validacion1(A)
    if A == 'R' or A=='I' or A=='C':
        break
    
TipoDeCir(A)
#CIRCUITO RESISTIVO------------------------------------------------------------------------------
if TipoDeCir(A) == 'R':
    print ('--------CIRCUITO RESISTIVO--------')
    print('\n')
    R1 = int(input('Cuantas Resistencias desea que tenga el circuito?: '))
    r = str(input('Desea que los valores sean ingresados manualmente(M) o sean valores random(R)?:'))
    
    if r =='M':
        
        for i in range (R1):
            Con = str(input('Como quiere conectar la resistencia: Serie(S) o Paralelo(P)?: '))
            n = int(input('Ingrese el valor de la resistencia(ohmios): '))
            if Con == 'S':
                Serie.append(n)
            elif Con == 'P':
                Paralelo.append(n)
            
        ResisSerie = sum(Serie)
        para = np.prod(Paralelo)
        sumatr = sum(Paralelo)
        ResisPara = para/sumatr
        Requivalente = [ResisSerie,ResisPara]
         
        REQ = sum(Requivalente)
#FUENTES---------------------------------------------------------------------------------------------    
        F1 = int(input('Cuantas fuentes desea que tenga el circuito?: '))
        if F1 > 1:
            for i in range (F1):
                Tip = str(input('Que tipo de fuente desea que tenga el circuito: Voltaje(V) o Corriente(C)?: '))
                f = int(input('Ingrese el valor de la fuente: '))
                if Tip == 'V':
                    Voltaje.append(f)
                elif Tip == 'C':
                    Corriente.append(f)
                    
            while True:
                Fv = str(input('Como desea que se conecten las fuentes de Voltaje? Serie(S) o Paralelo(P): '))
                if Fv == 'P':
                    if len(Voltaje) == len(set(Voltaje)):
                        print('NO SE PUEDEN CONECTAR FUENTES EN PARALELO CON DISTINTOS VOLTAJES') 
                    else:
                        fuentesV(Fv, Voltaje)
                        break
                elif Fv == 'S':
                    fuentesV(Fv, Voltaje)
                    break
                
            while True:
                Fc = str(input('Como desea que se conecten las fuentes de Corriente? Serie(S) o Paralelo(P): '))
                if Fc == 'P':
                    if len(Voltaje) == len(set(Corriente)):
                        print('NO SE PUEDEN CONECTAR FUENTES EN PARALELO CON DISTINTOS CORRIENTE') 
                    else:
                        fuentesC(Fc, Corriente)
                        break
                elif Fc == 'S':
                    fuentesC(Fc, Corriente)
                    break
                
        elif F1 == 1:
            Tip = str(input('Que tipo de fuente desea que tenga el circuito: Voltaje(V) o Corriente(C)?: '))
            f = int(input('Ingrese el valor de la fuente: '))
            if Tip == 'V':
                Voltaje.append(f)
            elif Tip == 'C':
                Corriente.append(f)
        
                
           
#Random-----------------------------------------------------------------------------------------------                    
    elif r == 'R':
        for i in range (R1):
            Con = str(input('Como quiere conectar la resistencia: Serie(S) o Paralelo(P)?: '))
            n = random.randint(1,100)
            if Con == 'S':
                Serie.append(n)
            elif Con == 'P':
                Paralelo.append(n)
        ResisSerie = sum(Serie)
        para = np.prod(Paralelo)
        ResisPara = para/ResisSerie
        Requivalente = [ResisSerie,ResisPara]
         
        REQ = sum(Requivalente)
                
        F1 = int(input('Cuantas fuentes desea que tenga el circuito?: '))
        if F1 > 1:
            for i in range (F1):
                Tip = str(input('Que tipo de fuente desea que tenga el circuito: Voltaje(V) o Corriente(C)?: '))
                f = random.randint(1,50)
                if Tip == 'V':
                    Voltaje.append(f)
                elif Tip == 'C':
                    Corriente.append(f)
            print('Las fuentes se conectaron en serie automaticamente')
            
            Fv = 'S'
            fuentesV(Fv, Voltaje)
            
            
            Fc = 'S'
            fuentesC(Fc, Corriente)
            
        elif F1 == 1:
            Tip = str(input('Que tipo de fuente desea que tenga el circuito: Voltaje(V) o Corriente(C)?: '))
            f = random.randint(1,50)
            if Tip == 'V':
                Voltaje.append(f)
            elif Tip == 'C':
                Corriente.append(f)
    print()
#-------------------------------------------------------------------------------------------------------    
    if r =='M':
        print('La resistencia equivalente es:',REQ,'ohmios')
        if F1 > 1:
            if fuentesV(Fv, Voltaje) == 0:
                print('El voltaje del circuito es:',fuentesC(Fc, Corriente)*REQ,'V')
                print('La corriente del circuito es:',fuentesC(Fc, Corriente),'A')
            elif fuentesC(Fc, Corriente) == 0:
                print('El voltaje del circuito es:',fuentesV(Fv, Voltaje),'V')
                print('La corriente del circuito es:',fuentesV(Fv, Voltaje)/REQ,'A')
            else:
                print('El voltaje del circuito es:',fuentesV(Fv, Voltaje),'V')
                print('La corriente del circuito es:',fuentesC(Fc, Corriente),'A')
                
        elif F1 == 1:
            if Tip == 'V': 
                print('El voltaje del circuito es:',f,'V')
                print('La corriente del circuito es:',f/REQ,'A')
            elif Tip == 'C':
                print('La corriente del circuito es:',f,'A')
                print('El voltaje del circuito es:',f * REQ,'V')
                
    elif r == 'R':
        print('La resistencia equivalente es:',REQ,'ohmios')
        if F1 > 1:
            if fuentesV(Fv, Voltaje) == 0:
                print('El voltaje del circuito es:',fuentesC(Fc, Corriente)*REQ,'V')
                print('La corriente del circuito es:',fuentesC(Fc, Corriente),'A')
            elif fuentesC(Fc, Corriente) == 0:
                print('El voltaje del circuito es:',fuentesV(Fv, Voltaje),'V')
                print('La corriente del circuito es:',fuentesV(Fv, Voltaje)/REQ,'A')
            else:
                print('El voltaje del circuito es:',fuentesV(Fv, Voltaje),'V')
                print('La corriente del circuito es:',fuentesC(Fc, Corriente),'A')
                
        elif F1 == 1:
            if Tip == 'V': 
                print('El voltaje del circuito es:',f,'V')
                print('La corriente del circuito es:',f/REQ,'A')
            elif Tip == 'C':
                print('La corriente del circuito es:',f,'A')
                print('El voltaje del circuito es:',f * REQ,'V')
    esquema_del_circuito(Serie, Paralelo,Voltaje,Corriente)
    turtle.mainloop()
    turtle.bye()
    
    
    
    
elif TipoDeCir(A) == 'I':
    print ('--------CIRCUITO INDUCTIVO--------')
    print('\n')
    r = str(input('Desea que los valores sean ingresados manualmente(M) o sean valores random(R)?:'))
    
    if r == 'M':   
        I1 = int(input('Cuantos Inductores desea que tenga el circuito?: '))
        for i in range(I1):
            Con = str(input("Como desea que se conecte el inductor, Serie(S) o Paralelo(P): "))
            n = int(input('Ingrese el valor del inductor(Hr): '))
            if Con == 'S':
                Serie.append(n)
            elif Con == 'P':
                Paralelo.append(n)
        ResisSerie = sum(Serie)
        para = np.prod(Paralelo)
        sumati = sum(Paralelo)
        ResisPara = para/sumati
        Requivalente = [ResisSerie,ResisPara]
        
        REQ = sum(Requivalente)
        
        F1 = int(input('Cuantas fuentes desea que tenga el circuito?: '))
        if F1 > 1:
            for i in range (F1):
                Tip = str(input('Que tipo de fuente desea que tenga el circuito: Voltaje(V) o Corriente(C)?: '))
                f = int(input('Ingrese el valor de la fuente: '))
                if Tip == 'V':
                    Voltaje.append(f)
                elif Tip == 'C':
                    Corriente.append(f)
            while True:
                Fv = str(input('Como desea que se conecten las fuentes de Voltaje? Serie(S) o Paralelo(P): '))
                if Fv == 'P':
                    if len(Voltaje) == len(set(Voltaje)):
                        print('NO SE PUEDEN CONECTAR FUENTES EN PARALELO CON DISTINTOS VOLTAJES') 
                    else:
                        fuentesV(Fv, Voltaje)
                        break
                elif Fv == 'S':
                    fuentesV(Fv, Voltaje)
                    break
                
            while True:
                Fc = str(input('Como desea que se conecten las fuentes de Corriente? Serie(S) o Paralelo(P): '))
                if Fc == 'P':
                    if len(Voltaje) == len(set(Corriente)):
                        print('NO SE PUEDEN CONECTAR FUENTES EN PARALELO CON DISTINTOS CORRIENTE') 
                    else:
                        fuentesC(Fc, Corriente)
                        break
                elif Fc == 'S':
                    fuentesC(Fc, Corriente)
                    break
                
        elif F1 == 1:
            Tip = str(input('Que tipo de fuente desea que tenga el circuito: Voltaje(V) o Corriente(C)?: '))
            f = int(input('Ingrese el valor de la fuente: '))
            if Tip == 'V':
                Voltaje.append(f)
            elif Tip == 'C':
                Corriente.append(f)
    
    elif r == 'R':
        I1 = int(input('Cuantos Inductores desea que tenga el circuito?: '))
        for i in range (I1):
            Con = str(input('Como quiere conectar los inductores: Serie(S) o Paralelo(P)?: '))
            n = random.randint(1,100)
            if Con == 'S':
                Serie.append(n)
            elif Con == 'P':
                Paralelo.append(n)
        ResisSerie = sum(Serie)
        para = np.prod(Paralelo)
        ResisPara = para/ResisSerie
        Requivalente = [ResisSerie,ResisPara]
         
        REQ = sum(Requivalente)
                
        F1 = int(input('Cuantas fuentes desea que tenga el circuito?: '))
        if F1 > 1:
            for i in range (F1):
                Tip = str(input('Que tipo de fuente desea que tenga el circuito: Voltaje(V) o Corriente(C)?: '))
                f = random.randint(1,50)
                if Tip == 'V':
                    Voltaje.append(f)
                elif Tip == 'C':
                    Corriente.append(f)
            print('Las fuentes se conectaron en serie automaticamente')
            
            Fv = 'S'
            fuentesV(Fv, Voltaje)
            
            
            Fc = 'S'
            fuentesC(Fc, Corriente)
            
        elif F1 == 1:
            Tip = str(input('Que tipo de fuente desea que tenga el circuito: Voltaje(V) o Corriente(C)?: '))
            f = random.randint(1,50)
            if Tip == 'V':
                Voltaje.append(f)
            elif Tip == 'C':
                Corriente.append(f)
    print()
    
    if r =='M':
        print('La inductancia equivalente es:',REQ,'Henrios')
        if F1 > 1:
            if fuentesV(Fv, Voltaje) == 0:
                print('El voltaje del circuito es:',fuentesC(Fc, Corriente)*REQ,'V')
                print('La corriente del circuito es:',fuentesC(Fc, Corriente),'A')
                print('La potencia del circuito es:',(fuentesC(Fc, Corriente)*REQ)*fuentesC(Fc, Corriente),'W')
            elif fuentesC(Fc, Corriente) == 0:
                print('El voltaje del circuito es:',fuentesV(Fv, Voltaje),'V')
                print('La corriente del circuito es:',fuentesV(Fv, Voltaje)/REQ,'A')
                print('La potencia del circuito es:',fuentesV(Fv, Voltaje)*(fuentesV(Fv, Voltaje)/REQ),'W')
            else:
                print('El voltaje del circuito es:',fuentesV(Fv, Voltaje),'V')
                print('La corriente del circuito es:',fuentesC(Fc, Corriente),'A')
                print('La potencia del circuito es:',fuentesV(Fv, Voltaje)*fuentesC(Fc, Corriente),'W')
                
        elif F1 == 1:
            if Tip == 'V': 
                print('El voltaje del circuito es:',f,'V')
                print('La corriente del circuito es:',f/REQ,'A')
                print('La potencia del circuito es:',f*(f/REQ),'W')
                
            elif Tip == 'C':
                print('La corriente del circuito es:',f,'A')
                print('El voltaje del circuito es:',f * REQ,'V')
                print('La potencia del circuito es:',f*(f*REQ),'W')
    
    elif r == 'R':
        print('La inductancia equivalente es:',REQ,'Henrios')
        if F1 > 1:
            if fuentesV(Fv, Voltaje) == 0:
                print('El voltaje del circuito es:',fuentesC(Fc, Corriente)*REQ,'V')
                print('La corriente del circuito es:',fuentesC(Fc, Corriente),'A')
                print('La potencia del circuito es:',(fuentesC(Fc, Corriente)*REQ)*fuentesC(Fc, Corriente),'W')
            elif fuentesC(Fc, Corriente) == 0:
                print('El voltaje del circuito es:',fuentesV(Fv, Voltaje),'V')
                print('La corriente del circuito es:',fuentesV(Fv, Voltaje)/REQ,'A')
                print('La potencia del circuito es:',fuentesV(Fv, Voltaje)*(fuentesV(Fv, Voltaje)/REQ),'W')
            else:
                print('El voltaje del circuito es:',fuentesV(Fv, Voltaje),'V')
                print('La corriente del circuito es:',fuentesC(Fc, Corriente),'A')
                print('La potencia del circuito es:',fuentesV(Fv, Voltaje)*fuentesC(Fc, Corriente),'W')
                
        elif F1 == 1:
            if Tip == 'V': 
                print('El voltaje del circuito es:',f,'V')
                print('La corriente del circuito es:',f/REQ,'A')
                print('La potencia del circuito es:',f*(f/REQ),'W')
            elif Tip == 'C':
                print('La corriente del circuito es:',f,'A')
                print('El voltaje del circuito es:',f * REQ,'V')
                print('La potencia del circuito es:',f*(f*REQ),'W')
                
    esquema_Inductivo(Serie, Paralelo,Voltaje,Corriente)
    turtle.mainloop()
    turtle.bye()
    
    
elif TipoDeCir(A) == 'C':
    print('-----------CIRCUITO CAPACITIVO-------------------')
    print('\n')
    print()
    r = str(input('Desea que los valores sean ingresados manualmente(M) o sean valores random(R)?:'))
    
    if r == 'M':   
        I1 = int(input('Cuantos Capacitores desea que tenga el circuito?: '))
        for i in range(I1):
            Con = str(input("Como desea que se conecte el capacitor, Serie(S) o Paralelo(P): "))
            n = int(input('Ingrese el valor del capacitor(Faradios): '))
            if Con == 'S':
                Serie.append(n)
            elif Con == 'P':
                Paralelo.append(n)
                
        para = np.prod(Serie) 
        sumatl = sum(Serie)
        ResisSerie = para/sumatl
        
        ResisPara = sum(Paralelo)
        Requivalente = [ResisSerie,ResisPara]
        
        REQ = sum(Requivalente)
        
        F1 = int(input('Cuantas fuentes desea que tenga el circuito?: '))
        if F1 > 1:
            for i in range (F1):
                Tip = str(input('Que tipo de fuente desea que tenga el circuito: Voltaje(V) o Corriente(C)?: '))
                f = int(input('Ingrese el valor de la fuente: '))
                if Tip == 'V':
                    Voltaje.append(f)
                elif Tip == 'C':
                    Corriente.append(f)
            while True:
                Fv = str(input('Como desea que se conecten las fuentes de Voltaje? Serie(S) o Paralelo(P): '))
                if Fv == 'P':
                    if len(Voltaje) == len(set(Voltaje)):
                        print('NO SE PUEDEN CONECTAR FUENTES EN PARALELO CON DISTINTOS VOLTAJES') 
                    else:
                        fuentesV(Fv, Voltaje)
                        break
                elif Fv == 'S':
                    fuentesV(Fv, Voltaje)
                    break
                
            while True:
                Fc = str(input('Como desea que se conecten las fuentes de Corriente? Serie(S) o Paralelo(P): '))
                if Fc == 'P':
                    if len(Voltaje) == len(set(Corriente)):
                        print('NO SE PUEDEN CONECTAR FUENTES EN PARALELO CON DISTINTOS CORRIENTE') 
                    else:
                        fuentesC(Fc, Corriente)
                        break
                elif Fc == 'S':
                    fuentesC(Fc, Corriente)
                    break
                
        elif F1 == 1:
            Tip = str(input('Que tipo de fuente desea que tenga el circuito: Voltaje(V) o Corriente(C)?: '))
            f = int(input('Ingrese el valor de la fuente: '))
            if Tip == 'V':
                Voltaje.append(f)
            elif Tip == 'C':
                Corriente.append(f)
                
    elif r == 'R':
        I1 = int(input('Cuantos Capacitores desea que tenga el circuito?: '))
        for i in range (I1):
            Con = str(input('Como quiere conectar los capacitores: Serie(S) o Paralelo(P)?: '))
            n = random.randint(1,100)
            if Con == 'S':
                Serie.append(n)
            elif Con == 'P':
                Paralelo.append(n)
                
        para = np.prod(Serie) 
        sumatl = sum(Serie)
        ResisSerie = para/sumatl
        
        ResisPara = sum(Paralelo)
        Requivalente = [ResisSerie,ResisPara]
        
        REQ = sum(Requivalente)
        
        F1 = int(input('Cuantas fuentes desea que tenga el circuito?: '))
        if F1 > 1:
            for i in range (F1):
                Tip = str(input('Que tipo de fuente desea que tenga el circuito: Voltaje(V) o Corriente(C)?: '))
                f = random.randint(1,50)
                if Tip == 'V':
                    Voltaje.append(f)
                elif Tip == 'C':
                    Corriente.append(f)
            print('Las fuentes se conectaron en serie automaticamente')
            
            Fv = 'S'
            fuentesV(Fv, Voltaje)
            
            
            Fc = 'S'
            fuentesC(Fc, Corriente)
            
        elif F1 == 1:
            Tip = str(input('Que tipo de fuente desea que tenga el circuito: Voltaje(V) o Corriente(C)?: '))
            f = random.randint(1,50)
            if Tip == 'V':
                Voltaje.append(f)
            elif Tip == 'C':
                Corriente.append(f)
    print()
    
    if r =='M':
        print('La capacitancia equivalente es:',REQ,'Faradios')
        if F1 > 1:
            if fuentesV(Fv, Voltaje) == 0:
                print('El voltaje del circuito es:',fuentesC(Fc, Corriente)*REQ,'V')
                print('La corriente del circuito es:',fuentesC(Fc, Corriente),'A')
                print('La potencia del circuito es:',(fuentesC(Fc, Corriente)*REQ)*fuentesC(Fc, Corriente),'W')
            elif fuentesC(Fc, Corriente) == 0:
                print('El voltaje del circuito es:',fuentesV(Fv, Voltaje),'V')
                print('La corriente del circuito es:',fuentesV(Fv, Voltaje)/REQ,'A')
                print('La potencia del circuito es:',fuentesV(Fv, Voltaje)*(fuentesV(Fv, Voltaje)/REQ),'W')
            else:
                print('El voltaje del circuito es:',fuentesV(Fv, Voltaje),'V')
                print('La corriente del circuito es:',fuentesC(Fc, Corriente),'A')
                print('La potencia del circuito es:',fuentesV(Fv, Voltaje)*fuentesC(Fc, Corriente),'W')
                
        elif F1 == 1:
            if Tip == 'V': 
                print('El voltaje del circuito es:',f,'V')
                print('La corriente del circuito es:',f/REQ,'A')
                print('La potencia del circuito es:',f*(f/REQ),'W')
                
            elif Tip == 'C':
                print('La corriente del circuito es:',f,'A')
                print('El voltaje del circuito es:',f * REQ,'V')
                print('La potencia del circuito es:',f*(f*REQ),'W')
    
    elif r == 'R':
        print('La capacitancia equivalente es:',REQ,'Faradios')
        if F1 > 1:
            if fuentesV(Fv, Voltaje) == 0:
                print('El voltaje del circuito es:',fuentesC(Fc, Corriente)*REQ,'V')
                print('La corriente del circuito es:',fuentesC(Fc, Corriente),'A')
                print('La potencia del circuito es:',(fuentesC(Fc, Corriente)*REQ)*fuentesC(Fc, Corriente),'W')
            elif fuentesC(Fc, Corriente) == 0:
                print('El voltaje del circuito es:',fuentesV(Fv, Voltaje),'V')
                print('La corriente del circuito es:',fuentesV(Fv, Voltaje)/REQ,'A')
                print('La potencia del circuito es:',fuentesV(Fv, Voltaje)*(fuentesV(Fv, Voltaje)/REQ),'W')
            else:
                print('El voltaje del circuito es:',fuentesV(Fv, Voltaje),'V')
                print('La corriente del circuito es:',fuentesC(Fc, Corriente),'A')
                print('La potencia del circuito es:',fuentesV(Fv, Voltaje)*fuentesC(Fc, Corriente),'W')
                
        elif F1 == 1:
            if Tip == 'V': 
                print('El voltaje del circuito es:',f,'V')
                print('La corriente del circuito es:',f/REQ,'A')
                print('La potencia del circuito es:',f*(f/REQ),'W')
            elif Tip == 'C':
                print('La corriente del circuito es:',f,'A')
                print('El voltaje del circuito es:',f * REQ,'V')
                print('La potencia del circuito es:',f*(f*REQ),'W')
    
    esquema_capacitivo(Serie, Paralelo, Voltaje, Corriente)
    turtle.mainloop()
    turtle.bye()
    
        
    


        
        
    
    
    




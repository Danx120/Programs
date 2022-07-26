
import random
import numpy as np
import turtle

FyP  = turtle.Turtle()
#FUNCIONES--------------------------------------------------------------
def matriz(f,c,MATRIZ):
    for i in range(f):
        for j in range(c):
            x = random.randint(10,100)
            MATRIZ[i][j] = x
    return MATRIZ
def impresion(MATRIZ,f,c):
    for i in range(f):
        print('\n')
        for j in range(c):
            print(MATRIZ[i][j],'|',end= '  ')
            
def FbPl0912():
    FyP.pencolor('pink')
    FyP.left(45)
    FyP.forward(100)
    FyP.right(90)
    FyP.forward(150)
    FyP.right(90)
    FyP.forward(250)
    FyP.pencolor('brown')
    FyP.right(90)
    FyP.forward(250)
    FyP.right(90)
    FyP.forward(150)
    FyP.right(90)
    FyP.forward(100)

        
#MENU--------------------------------------------------------------------
print('ALGEBRA LINEAL')
print('\n')

print('Operaciones con matrices')


print('Este programa solo trabajara con matrices cuadradas')


print('Las operaciones se realizaran con dos matrices')
print('\n')
print()
#PROGRAMA----------------------------------------------------------------------------
while True:
      f=int(input("ingresar número de filas:"))
      if f<2 or f>30:
          print("La matriz no puede tener menos de 2 filas ni mas de 30")
      else:
          break
while True:
      c=int(input("ingresar número de columnas:"))
      if c<2 or c>30:
          print("La matriz no puede tener menos de 2 columnas ni mas de 30")
      else:
          break
MoR = str(input('Como desea que sean ingresados los datos en la matriz, Manual(m) o Random(r): '))

MATRIZ1 = [[int()for i in range(c)]for j in range(f)]
MATRIZ2 = [[int()for i in range(c)]for j in range(f)]



if MoR == 'r':
    matriz(f, c, MATRIZ1)
    matriz(f, c, MATRIZ2)
elif MoR == 'm':
    for i in range(f):
        for j in range(c):
            x = int(input('Ingrese un numero'))
            MATRIZ1[i][j] = x
    for i in range(f):
        for j in range(c):
            y = int(input('Ingrese un numero'))
            MATRIZ2[i][j] = y
P = np.array(MATRIZ1)
F = np.array(MATRIZ2)
print()
print('LAS MATRICES SON ESTAS:')
impresion(MATRIZ1, f, c)
print()
impresion(MATRIZ2, f, c)

print('\n')

Pauli = ['Para la matriz inversa digite(f)','Para el determinante de la matriz digite(i)','Para el producto vectorial digite(p)','Para matriz traspuesta digite (t)', 'Para hacer una suma digite(s)', 'Para hacer una resta digite (r)','Para hacer una multiplicación digite (m)','Para hacer la división digite (d)']
for i in range(len(Pauli)):
    print(Pauli[i])
print('\n')    
rt = str(input('Escoja la operacion que desea ejecutar: '))

if rt == 's':
    print('La suma de las matrices es:')
    print(P + F)

elif rt == 't':
    print('La matriz transpuesta de las matrices son:')
    print(P.T)
    print()
    print(F.T)

elif rt == 'r':
    print('La resta de las matrices es:')
    print(P-F)

elif rt == 'm':
    print('La multiplicacion de las matrices es:')
    print(P*F)

elif rt == 'd':
    print('La division de las matrices es:')
    print(P/F)
elif rt == 'p':
    print('EL producto vectorial de las matrices es:')
    print(P.dot(F))
elif rt == 'i':
    print('El determinante de la matriz es:')
    print(np.linalg.det(P))
    print()
    print(np.linalg.det(F))
elif rt == 'f':
    print('La matriz inversa de cada matriz es:')
    print(np.linalg.inv(P))
    print()
    print(np.linalg.inv(F))

FbPl0912()
turtle.mainloop()
turtle.bye()







      



    
    
    
  






fila = 4
columna = 4

M = [0] * fila

for i in range (columna):
    M[i] = [0] * columna
    
for i in range(fila):
    for j in range(columna):
        num=int(input('Fila'' {},Columna {}:'.format(i+1, j+1)))
        M[i][j] = (num)

print()

for i in range(fila):
    for j in range(columna):
        print(M[i][j],end = ' ')
    print(' ')
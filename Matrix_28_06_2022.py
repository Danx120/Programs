
matrix = [[1,2,3,4],
          [4,5,6,7],
          [8,9,10,11]]

print(matrix[0][0])
print(matrix[2][2])

filas = 3
columnas = 4

for i in range(filas):
    for j in range(columnas):
        print(matrix[i][j],end = ' ')
    print(' ')
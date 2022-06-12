#Fabrica de chocolates
#Autor: Daniel Calapiña
chocolates=int(input('Ingrese el numero de chocolates fabricados en un dia'))
cajas=chocolates//15
sobrantes=chocolates%15
print('El numero de cajas completadas en un dia es:',cajas)
print('El numero de chocolates sobrantes es:',sobrantes)

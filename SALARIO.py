#Calculo del salario
#Autor: Daniel Calapiña 
nombre=input('ingrese el nombre:')
horas=int(input('ingresar horas:'))
precio=int(input('ingresar precio:'))
bruto=horas*precio 
tasas=0.25*bruto
neto=bruto-tasas 
print('El salario bruto es:',bruto)
print('las tasas son:',tasas)
print('El salario neto es:',neto)

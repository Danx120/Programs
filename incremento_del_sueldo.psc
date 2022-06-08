Algoritmo incremento_del_sueldo
	Definir sueldo,incremento,total Como Real
	Definir continuar Como Caracter
	Repetir
		Escribir 'Ingrese el sueldo del empleado'
		Leer sueldo
		incremento=sueldo*0.08
		total=sueldo+incremento
		Escribir 'El total es:',total
		Escribir 'El total a pagar es:',total
		Escribir 'Si desea salir digite si y para continuar digite cualquier caracter'
		Leer continuar
	Hasta Que continuar='si' o continuar='SI' o continuar='Si' o continuar='sI'
	
FinAlgoritmo

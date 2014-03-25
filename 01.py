# -*- coding: utf-8 -*-
def calcula_dc ( lista ):
	""" Calcula el dígito de control de una CCC.
	Recibe una lista con 10 numeros enteros y devuelve el DC
	correspondiente """
	pesos = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
	aux = []
	for i in range (10):
		aux. append ( lista [i]* pesos [i])
	resto = 11 - sum(aux) %11
	if resto == 10:
		return 1
	elif resto == 11:
		return 0
	else:
		return resto
	
recibe=raw_input("Introduzca los digitos de control con el siguiente formato AAAA-BBBB-CC-DDDDDDDDDD: ").split("-")
entidadyoficina=[0,0]
for i in ccc[]

recibe1=int(recibe)

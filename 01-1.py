def calcula_dc(lista):
	pesos = [1, 2, 4, 8, 5, 10, 9, 7, 3, 6]
	aux = []
	for i in range(10):
		aux.append(lista[i]*pesos[i])
	resto = 11 - sum(aux)%11
	if resto == 10:
		return 1
	elif resto == 11:
		return 0
	else:
		return resto

ccc = raw_input("Dame tu numero de cuenta corriente (AAAA-BBBB-CC-DDDDDDDDDD): ").split("-")
entidadyoficina = [0, 0]
for i in ccc[0]+ccc[1]:
	entidadyoficina.append(int(i))
cuenta = []
for i in ccc[3]:
	cuenta.append(int(i))

dc = "%s%s" % (str(calcula_dc(entidadyoficina)),str(calcula_dc(cuenta)))
print "el digito de control es: %s" % dc
if dc ==ccc[2]:
	print "El digito de control es correcto"
else:
	print "El digito de control es incorrecto"




Boletin_3
=========

Boletin 3 de ejercicios simples de Python.

1. El Código Cuenta Cliente (CCC) es el código que identifica en España las cuentas cor-
rientes de los clientes de bancos. El CCC tiene 20 dígitos en formato AAAA-BBBB-CC-
DDDDDDDDDD.
◦ AAAA son cuatro dígitos que identifican la entidad bancaria.
◦ BBBB son cuatro dígitos que identifican la oficina.
◦ CC se denomina dígito de control (DC).
◦ DDDDDDDDDD son 10 dígitos de la cuenta del cliente en el banco.

Según la Wikipedia:

Los dígitos situados en las posiciones novena y décima se generan a partir
de los demás dígitos del CCC, permitiendo comprobar la validez del mismo
y reducir la posibilidad de errores de manipulación. El primero de ellos val-
ida conjuntamente los códigos de entidad y de oficina; el segundo, valida el
número de cuenta.

Cada uno de los dígitos del DC se calcula utilizando el mismo algoritmo, para lo que se
complementa con dos ceros a la izquierda la entidad y oficina.
La siguiente función en Python calcula el DC correspondiente para una lista de 10
número enteros:

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
Por ejemplo:
>>> lista = [1, 6, 7, 0, 0, 0, 0, 3, 3, 2]
>>> calcula_dc ( lista )

Escribe un programa que pida al usuario un CCC en el formato arriba indicado y com-
pruebe su validez.


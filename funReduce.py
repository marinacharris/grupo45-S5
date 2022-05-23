# Sintaxis
# reduce(funcion, objeto iterable)
from functools import reduce

lista= [1,2,3,7,2]
acumulador= 0
for i in lista:
    acumulador +=i
print(acumulador)

resultado = reduce(lambda acumulador, numero: acumulador + numero, lista)
print(resultado)



# sintaxis
# map(funcion, objeto iterable)
from math import pow

def cuadrado(numero):
    return numero**2
lista = [4,2,7,8,5,21,4]
cuadrados = list(map(cuadrado,lista))
print(cuadrados)

cuadrados2 = list(map(lambda numero: numero**2 , lista))
print(cuadrados2)

bases= [2,4,5,7,1,2,0]
potencias = [2,3,1,0,4,5,10]

resultado = list(map(pow,bases,potencias))
print(resultado)
# sintaxis
# map(funcion, objeto iterable)
from math import pow
from functools import reduce
# programacion imperativa
lista = [4,2,7,8,5,21,4]
cuadrados = []
for i in lista:
    cuadrados.append(i**2)
print(cuadrados)

# programacion funcional
def cuadrado(numero):
    return numero**2
lista = [4,2,7,8,5,21,4]
cuadrados = list(map(cuadrado,lista))
print(cuadrados)

# programacion funcional con lambda
cuadrados2 = list(map(lambda numero: numero**2 , lista))
print(cuadrados2)

bases= [2,4,5,7,1,2,0]
potencias = [2,3,1,0,4,5,10]

resultado = list(map(pow,bases,potencias))
print(resultado)

lista = [
    [1525, [4, 2500],[3,8500],[5,12600]], #[No. factura, [cantidad. precio unidad]...]
    [1520, [3, 2500],[8,12600]],
    [1622, [1, 2500],[5,8500],[2,12600]]    
]
# Crear una lista de listas: [[No. factura, total1, total2,...totaln],...[]]
total= list(map(lambda x: [x[0]]+ list(map(lambda y: y[0]*y[1] ,x[1:])),lista))
print(total)
# Crear una lista de listas: [[No. factura, total factura], ...[]]
total = list(map(lambda x: [x[0]]+ [reduce(lambda y,z: y+z,x[1:])],total))
print(total)



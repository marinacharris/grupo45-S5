# Sintaxis
# filter(funcion, objeto iterable)

lista = [2,4,85,1,0,5,3]

def pares(numero):
    return numero%2 == 0 
listaPares = tuple(filter(pares,lista))
print(listaPares)

listaPares2 = tuple(filter(lambda numero: numero%2 == 0,lista))
print(listaPares2)
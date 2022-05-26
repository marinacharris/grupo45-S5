lista1 =[2,5,3,1]
lista2 = [5,2,4,8]

lista3 = lista1 + lista2
print(lista3)
print(lista3[0:3])
print(lista3[:3])
print(lista3[4:])
print(lista3[2:5])

a=5
a= a+1 

# if en una sola linea, se puede si el interior de if es de una sola instruccion
# ejemplo:

a = 5
if a == 5:
    print('ok')
else:
    print('error')
    
print('ok') if a==5 else print('error')

#Comprensión de listas:
# método tradicional
lista = [4,2,7,8,5,21,4]
cuadrados = []
for i in lista:
    cuadrados.append(i**2)
print(cuadrados)

#comprensión de listas
cuadrados2 = [i**2 for i in lista]
print(cuadrados2)

a = 58695656.456454654
b = round(a,2)
print(f'El numero es {b:,.2F}')
    


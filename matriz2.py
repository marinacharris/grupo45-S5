import numpy as np
# matriz de solo ceros
matriz = np.zeros((4,4), dtype=np.int8)
print(matriz)

# matriz de solo unos
matriz = np.ones((2,2))
print(matriz)

# matriz de un valor
matriz = np.full((2,2),True)
print(matriz)

# matriz de número aleatorios
matriz = np.random.random((3,3))
print(matriz)

# matriz identidad
matriz = np.eye(5)
print(matriz)
#rebanados
matriz2 = np.array([[5,6,8],[1,2,8],[9,9,9]])
print(matriz2)
matriz3 = matriz2[:2,:2]
print(matriz3)
matriz4 = matriz2[1:,1:]
print(matriz4)
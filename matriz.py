import numpy as np
matriz1 = np.array([4,5,8])
print(matriz1, matriz1.shape, type(matriz1), matriz1[2])

matriz2 = np.array([[1,2,6],[5,8,4]])
print(matriz2, matriz2.shape, type(matriz2), matriz2[1,1])

print("___________________________________________")
matriz3 = np.array([[[1,2,5,8],[5,8,2,3]],
                    [[5,8,3,9],[3,4,5,20]],
                    [[5,8,2,1],[6,5,8,9]]])
print(matriz3, matriz3.shape, matriz3[1,1,3])

matriz3[1,1,3] = 50
print(matriz3)

matriz4 = np.array([[1,2],[5,8]])
matriz5 = np.array([[7,4],[3,1]])
print(matriz4)
print(matriz5)
# Se puden realizar diversas operaciones aritméticas con las matrices
print(matriz4 * matriz5)
print(np.multiply(matriz4, matriz5))




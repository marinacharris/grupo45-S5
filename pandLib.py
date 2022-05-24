import pandas as pd
diccionario = {
    'a':1,
    'b':2,
    'C':3
}
serie = pd.Series(data=diccionario, index=list(diccionario.keys()))
print(serie)
print(serie[1])
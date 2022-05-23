# *args, **kwargs

def suma(a,b):
    return a+b

print(suma(8,6))


def suma2(*args):
    total = 0
    for i in args:
        total +=i
    return total

print(suma2(4,7,8,1))
print(suma2(1,2,3))
print(suma2(9,2,5,8,4,5,9,7,8,5,1))

def suma3(**kwargs):
    total = 0
    for i in kwargs:
        total += kwargs[i]
    return total

print(suma3(A=1, B=20, C=30))
print(suma3(A=20, B=20, C=30, D=1000))
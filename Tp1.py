 #1. Definir una función max() que tome como argumento dos números y devuelva el
#mayor de ellos.

def maxuno (n1, n2):
    if n1>= n2:
        return n1
    else:
        return n2



a=4
b=7

print(maxuno(a,b))

assert maxuno(a, b) == 7
assert maxuno(a, b) != 8
assert maxuno(a, b) != 4

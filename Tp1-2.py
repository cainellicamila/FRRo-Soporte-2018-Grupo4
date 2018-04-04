#2. Definir una función max_de_tres(), que tome tres números como argumentos y
#devuelva el mayor de ellos. 

def maxtres(n1,n2,n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3

a = 4
b = 7
c = 10

print(maxtres(a,b,c))

assert maxtres(a, b, c) == 10
assert maxtres(a, b, c) != 8
assert maxtres(a, b, c) != 4

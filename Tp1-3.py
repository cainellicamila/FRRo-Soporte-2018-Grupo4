#3. Definir una función que calcule la longitud de una lista o una cadena dada.

a = "Soporte"

def cantlet(n):
    c=0
    for i in n:
        c = c + 1
    return c

print(cantlet(a))

assert cantlet(a) == 7
assert cantlet(a) != 9
assert cantlet(a) != 4

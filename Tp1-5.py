#5. Escribir una función multip() que multiplique respectivamente todos los números de
#una lista. Por ejemplo: multip([1,2,3,4]) debería devolver 24.


def multip(n1,n2,n3,n4):
    tot = n1 * n2 * n3 * n4
    return tot


print(multip(1,2,3,4,))

assert (multip(1,2,3,4,) == 24)
assert (multip(1,2,3,4,) != 32)

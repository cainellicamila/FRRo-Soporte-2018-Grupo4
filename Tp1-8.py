# 8. Definir una función superposicion() que tome dos listas y devuelva True si tienen al
# menos 1 miembro en común o devuelva False de lo contrario. Escribir la función
# usando el bucle for anidado.

def superposicion(c1,c2):
    m = 0
    for i in c1:
        for k in c2:
            if i == k:
                m = 1
    if (m == 1):
        return True
    else:
        return False


a=[1, 2, 3, 4, 5]
b=[6, 7, 8, 9, 0]
print(superposicion(a,b))

assert (superposicion(a,b) == False)
assert (superposicion(a,b)!= True)

c=[1, 2, 3, 4, 5]
d=[6, 7, 8, 9, 1]
print(superposicion(c,d))

assert (superposicion(c,d) != False)
assert (superposicion(c,d)== True)

#Determinar la suma de todos los numeros de 1 a N. N es un número que se ingresa
#por consola.

def suma():
    n = int(input('ingresar N'))
    rta= 0.
    for i in range (n+1):
        rta=rta+i
    return rta

print(suma ())

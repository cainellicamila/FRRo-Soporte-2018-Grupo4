#Programe una funcion que determine si un numero entero suministrado como
#argumento es primo.

def esprimo (num):
    band="Si"
    for i in range(2, num):
        if num % i == 0:
            band="No"
    return(band)

print(esprimo(4))
print(esprimo(113))
print(esprimo(20))
print(esprimo(71))

assert esprimo(4) == "No"
assert esprimo(113) == "Si"


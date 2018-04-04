#Determinar la cantidad de dígitos de un número ingresado.

def cantdig (num):
    cant= 0
    numero= str(num)
    for i in numero:
        cant+=1
    return cant

print(cantdig(1234))

assert cantdig(1234) == 4
assert cantdig(1234) != 5

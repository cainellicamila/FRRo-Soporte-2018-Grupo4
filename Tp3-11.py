'''
Ejercicio 11
Programar un función Divide que ingresa dos valores x, y y devuelve el
cociente x/y. La función tiene que tener control de error, que imprima el nombre y el
tipo de error.
Ejemplos: Divide(6,0) Divide(60,”hola”) Divide(True,5)
'''

def Divide (x, y):
    try:
        res = x/y
    except ZeroDivisionError:
        print('Error en la division, se intenta dividir por cero')
    except TypeError:
        print('Se ingreso un tipo de dato no valido')
    else:
        print('El resultado es', res)

Divide(6,0)
Divide(60, 'hola')
Divide(True,5)

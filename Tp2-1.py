#Ejercicio 1
#Escribir una clase llamada rectángulo que contenga una base y una altura, y que contenga un
#método que devuelva el área del rectángulo.

class Rectangulo ():

    def __init__(self, b, a):
        self.base = b
        self.altura = a

    def calcarea (self):
        self.area = self.base * self.altura
        return self.area


rec = Rectangulo(4,5)

print ('El área del rectangulo es:',rec.calcarea())
assert rec.calcarea() == 20
assert rec.calcarea() != 19

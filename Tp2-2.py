'''
Ejercicio 2
Escribir una clase llamada círculo que contenga un radio, con un método que devuelva el área y
otro que devuelva el perímetro del círculo.
'''
from math import pi

class Circulo():

    def __init__(self, r):
        self.radio =r

    def calcarea (self):
        self.area = pi * self.radio **2
        return self.area

    def calcaperi (self):
        self.peri = 2 * pi * self.radio
        return self.peri


circu = Circulo(5)

print ('El área del circulo es:',circu.calcarea())
print ('El perimetro del circulo es:',circu.calcaperi())

assert circu.calcarea() == 78.53981633974483
assert circu.calcaperi() == 31.41592653589793
assert circu.calcarea() !=78
assert circu.calcaperi() != 31


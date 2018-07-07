# Escribir una clase Estudiante, que herede de Persona, y que agregue las siguientes condiciones:
# Atributos:
# - nombre de la carrera.
# - año de ingreso a la misma.
# - cantidad de materias de la carrera.
# - cantidad de materias aprobadas.
# Métodos:
# - avance(): indica que porcentaje de la carrera tiene aprobada.
# - edad_ingreso(): indica que edad tenia al ingresar a la carrera (basándose en el año actual).

from Tp2_3 import Persona

class Estudiante(Persona):

    def __init__(self, nom, ed, sex, pe, alt, car, an, cantm, cantap):
        Persona.__init__(self, nom, ed, sex, pe, alt)
        self.carrera=car
        self.anio=an
        self.cantidad_materias=cantm
        self.cantidad_aprobadas=cantap

    def avance (self):
        porc= ((self.cantidad_aprobadas*100)/self.cantidad_materias)
        return porc

    def edad_ingreso(self):
        edadinicial= self.edad - (2018-self.anio)
        return edadinicial

per=Estudiante('Camila', 20, 'F', 48,162, 'ISI', 2015, 41, 24)

print('Porcentaje de la carrera aprobado:', per.avance(), '%')
print('Al ingresar tenia',per.edad_ingreso(),'años')

assert per.avance() == 58.53658536585366
assert per.avance()!= 60
assert per.edad_ingreso()==17
assert per.edad_ingreso()!=19

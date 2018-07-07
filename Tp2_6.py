# Implementar la clase Persona con un constructor donde reciba una fecha de nacimiento.
# La clase además debe contener un método edad, que no recibe nada y devuelva la edad de la
# persona (entero).
# Para obtener la fecha actual, usar el método de clase "now" de la clase datetime (ya importada).

import datetime


class Persona:

    def __init__(self, fechanac):

        self.nacimiento = fechanac


    def calculo_edad(self):
        fechahoy = datetime.datetime.now()

        self.edad = (int(abs(fechahoy - self.nacimiento).days/365))

        return self.edad


per = Persona(datetime.datetime(1997, 6, 24))

edad = per.calculo_edad()

print(edad)

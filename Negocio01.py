# Implementar los metodos de la capa de negocio de socios.

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Datos.Datos01 import Socio, Base
from Datos.Datos02 import DatosSocio


class DniRepetido(Exception):
    pass


class LongitudInvalida(Exception):
    pass


class MaximoAlcanzado(Exception):
    pass


class NegocioSocio(object):

    MIN_CARACTERES = 3
    MAX_CARACTERES = 15
    MAX_SOCIOS = 200

    def __init__(self):
        self.datos = DatosSocio()

        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        self.session = DBSession()
        Base.metadata.create_all(engine)


    def buscar(self, id_socio):
        """
        Devuelve la instancia del socio, dado su id.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """

        soc = self.datos.buscar(id_socio)
        if soc:
            return soc
        else:
            return None


    def buscar_dni(self, dni_socio):
        """
        Devuelve la instancia del socio, dado su dni.
        Devuelve None si no encuentra nada.
        :rtype: Socio
        """

        soc=self.datos.buscar_dni(dni_socio)

        if soc:
            return soc
        else:
            return None



    def todos(self):
        """
        Devuelve listado de todos los socios.
        :rtype: list
        """
        socios=self.datos.todos()

        return socios

    def alta(self, socio):
        """
        Da de alta un socio.
        Se deben validar las 3 reglas de negocio primero.
        Si no validan, levantar la excepcion correspondiente.
        Devuelve True si el alta fue exitoso.
        :type socio: Socio
        :rtype: bool
        """

        if self.regla_1(socio) and self.regla_2(socio) and self.regla_3():
            self.datos.alta(socio)
            return True
        else:
            return False

    def baja(self, id_socio):
        """
        Borra el socio especificado por el id.
        Devuelve True si el borrado fue exitoso.
        :rtype: bool
        """
        b=self.datos.baja(id_socio)
        if b:
            return True
        else:
            return False

    def modificacion(self, socio):
        """
        Modifica un socio.
        Se debe validar la regla 2 primero.
        Si no valida, levantar la excepcion correspondiente.
        Devuelve True si la modificacion fue exitosa.
        :type socio: Socio
        :rtype: bool
        """
        if self.regla_2(socio):
            self.datos.modificacion(socio)
            return True
        else:
            return False

    def regla_1(self, socio):
        """
        Validar que el DNI del socio es unico (que ya no este usado).
        :type socio: Socio
        :raise: DniRepetido
        :return: bool
        """
        dni_rep = self.buscar_dni(socio.dni)
        if dni_rep:
            print('Dni repetido')
            raise DniRepetido('Dni repetido')

        else:
            return True

    def regla_2(self, socio):
        """
        Validar que el nombre y el apellido del socio cuenten con mas de 3 caracteres pero menos de 15.
        :type socio: Socio
        :raise: LongitudInvalida
        :return: bool
        """
        if (len(socio.nombre))< self.MIN_CARACTERES or (len(socio.nombre))>self.MAX_CARACTERES:
            print('Longitud de nombre invalida')
            raise LongitudInvalida('Longitud invalida')


        if (len(socio.apellido)) < self.MIN_CARACTERES or (len(socio.apellido)) > self.MAX_CARACTERES:
            print ('Longitud apellido invalida')
            raise LongitudInvalida('Longitud invalida')

        return True

    def regla_3(self):
        """
        Validar que no se esta excediendo la cantidad maxima de socios.
        :raise: MaximoAlcanzado
        :return: bool
        """
        if len(self.datos.todos())<self.MAX_SOCIOS:
            return True
        else:
            raise MaximoAlcanzado




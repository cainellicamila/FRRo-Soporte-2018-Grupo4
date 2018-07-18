# Implementar los casos de prueba descriptos.

import unittest

from Datos.Datos01 import Socio
from Negocio.Negocio01 import NegocioSocio, LongitudInvalida, DniRepetido, MaximoAlcanzado


class TestsNegocio(unittest.TestCase):

    def setUp(self):
        super(TestsNegocio, self).setUp()
        self.ns = NegocioSocio()

    def tearDown(self):
        super(TestsNegocio, self).tearDown()
        self.ns.datos.borrar_todos()

    def test_alta(self):
        # pre-condiciones: no hay socios registrados
        self.assertEqual(len(self.ns.todos()), 0)

        # ejecuto la logica
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        # post-condiciones: 1 socio registrado
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 1)

    def test_regla_1(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_1(valido))

        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(DniRepetido, self.ns.regla_1, invalido)

    def test_regla_2_nombre_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_nombre_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # nombre mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan Martin Pedro', apellido='Perez')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_menor_3(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido menor a 3 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='P')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_2_apellido_mayor_15(self):
        # valida regla
        valido = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        self.assertTrue(self.ns.regla_2(valido))

        # apellido mayor a 15 caracteres
        invalido = Socio(dni=12345678, nombre='Juan', apellido='Perez De Los Arroyos')
        self.assertRaises(LongitudInvalida, self.ns.regla_2, invalido)

    def test_regla_3(self):

        invalido = Socio(dni=12345678, nombre='J', apellido='Perez')
        self.assertRaises(MaximoAlcanzado, self.ns.regla_3, invalido)

    def test_baja(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)
        self.assertEqual(len(self.ns.todos()), 1)
        exito = self.ns.baja(socio.id)
        self.assertTrue(exito)
        self.assertEqual(len(self.ns.todos()), 0)

    def test_buscar(self):
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)
        self.assertEqual(len(self.ns.todos()), 1)

        exito = self.ns.buscar(socio.id)
        self.assertTrue(exito)

        fracaso = self.ns.buscar ('3')
        self.assertFalse(fracaso)

    def test_buscar_dni(self):

        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)
        self.assertEqual(len(self.ns.todos()), 1)

        exito = self.ns.buscar_dni(socio.dni)
        self.assertTrue(exito)

        fracaso = self.ns.buscar ('87654321')
        self.assertFalse(fracaso)

    def test_todos(self):

        socio1 = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito1 = self.ns.alta(socio1)
        socio2 = Socio(dni=87654321, nombre='Juan', apellido='Perez')
        exito2 = self.ns.alta(socio2)
        self.assertEqual(len(self.ns.todos()), 2)

    def test_modificacion(self):

        #socio a modificar
        socio = Socio(dni=12345678, nombre='Juan', apellido='Perez')
        exito = self.ns.alta(socio)

        #modifciacion correcta
        socio.nombre= 'Juana'
        exito = self.ns.modificacion(socio)
        self.assertTrue(exito)

        #nombre con menos de 3 letras
        socio.nombre = 'J'
        fracaso1= self.ns.modificacion(socio)
        self.assertFalse(fracaso1)

        #apellido con más de 15 letras
        socio.apellido='Perez de los arroyos'
        fracaso2=self.ns.modificacion(socio)
        self.assertFalse(fracaso2)



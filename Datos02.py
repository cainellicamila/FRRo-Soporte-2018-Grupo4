'''Crear una Clase Capa Datos Socio con los métodos necesarios para persistir y
recuperar los datos de la clase Socio , con los siguiente metodos
1) Alta de Socio se le pasa un Socio devuelve lógico si pudo darlo de alta
2) Modificar se le pasa Socio devuelve un lógico si pudo actualizar
3) Baja Socio se le pasa IDSocio devuelve un lógico si pudo darlo de baja
4) Buscar se le pasa IDSocio devuelve un socio con los datos .
5) Todos los Socios sin paramatro devuelve en una lista todos los socios .'''

import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Datos.Datos01 import Base, Socio

class DatosSocio(object):

    def __init__(self):
        engine = create_engine('sqlite:///socios.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        self.session = DBSession()
        Base.metadata.create_all(engine)

    def alta(self, nuevo_socio):
        try:
            self.session.add(nuevo_socio)
            self.session.commit()
            print('True')
            return nuevo_socio
        except:
            print('False')

    def modificacion(self, socio):
        try:
            self.session.query(Socio).filter(Socio.id == socio.id).update({Socio.dni:socio.dni, Socio.nombre:socio.nombre, Socio.apellido:socio.apellido})
            self.session.commit()
            print('True')
            return socio
        except:
            print('False')

    def baja (self, id_socio):

            s = self.session.query(Socio).filter_by(id=id_socio).first()
            if s:
                self.session.delete(s)
                return True
            else:
                return False

    def buscar(self, id_socio):
        return self.session.query(Socio).filter_by(id=id_socio).first()

    def todos(self):
        ps= self.session.query(Socio).all()
        return ps

    def borrar_todos(self):
        try:
            per=self.session.query(Socio).all()
            for s in per:
                self.session.delete(s)
            self.session.commit()
            return True

        except:
            return False

    def buscar_dni(self, dni):

        per=self.session.query(Socio).filter(Socio.dni==dni).first()

        return per

def pruebas():

    datos=DatosSocio()
    datos.borrar_todos()

    # alta
    socio = datos.alta(Socio(dni=12345678, nombre='Juan', apellido='Perez'))
    assert socio.id > 0

    # baja
    a = datos.baja(socio.id)
    assert a == True

    # buscar
    socio_2 = datos.alta(Socio(dni=12345679, nombre='Carlos', apellido='Perez'))
    assert datos.buscar(socio_2.id) == socio_2

    # buscar dni

    assert datos.buscar_dni(socio_2.dni) == socio_2

    # modificacion
    socio_3 = datos.alta(Socio(dni=12345680, nombre='Susana', apellido='Gimenez'))
    socio_3.nombre = 'Moria'
    socio_3.apellido = 'Casan'
    socio_3.dni = 13264587
    datos.modificacion(socio_3)
    socio_3_modificado = datos.buscar(socio_3.id)
    assert socio_3_modificado.id == socio_3.id
    assert socio_3_modificado.nombre == 'Moria'
    assert socio_3_modificado.apellido == 'Casan'
    assert socio_3_modificado.dni == 13264587

    # todos
    assert len(datos.todos()) == 2

    # borrar todos
    datos.borrar_todos()
    assert len(datos.todos()) == 0
    assert datos.borrar_todos()== True

if __name__ == '__main__':
    pruebas()


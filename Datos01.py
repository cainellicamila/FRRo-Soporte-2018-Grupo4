'''Usar Alchemy para acceder a los datos, usando Sqlite.
Crear una Modelo Socio que solo tenga propiedades equivalentes a los campos de
la Tabla Socio
Socio
Propiedades
 IdSoci
 DNI
 Nombre
 Apellido'''

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Socio(Base):
    __tablename__ = 'socios'

    id = Column(Integer, primary_key=True, autoincrement=True)
    dni = Column(Integer, nullable=False)
    nombre = Column(String(250), nullable=False)
    apellido = Column(String(250), nullable=False)



import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
Base = declarative_base()


class Favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    people_id = Column(Integer, ForeignKey('people.id'),nullable=True)
    planets_id = Column(Integer, ForeignKey('planets.id'),nullable=True)
    vehiculos_id = Column(Integer, ForeignKey('vehiculos.id'),nullable=True)
    usuarios_id = Column(Integer, ForeignKey('usuarios.id'),nullable=False)


class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    pasajeros = Column(Integer, nullable=False)
    usuarios_favoritos = relationship(Favoritos)
    

class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    height = Column(Integer, nullable=False)
    people_favoritos = relationship(Favoritos)

    
class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    climate = Column(String(250))
    population = Column(Integer, nullable=False)
    planets_favoritos = relationship(Favoritos)
    

class Vehiculos(Base):
    __tablename__ = 'vehiculos'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    model = Column(String(250))
    pasajeros = Column(Integer, nullable=False)
    vehiculos_favoritos = relationship(Favoritos)
    


    def to_dict(self):
        return {}
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
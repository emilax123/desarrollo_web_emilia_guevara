from sqlalchemy import create_engine, Column, Integer, BigInteger, String, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DB_NAME = "tarea2"
DB_USERNAME = "cc5002"
DB_PASSWORD = "programacionweb"
DB_HOST = "localhost"
DB_PORT = "3306"

DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL, echo=False, future=True)
Sessionlocal = sessionmaker(bind=engine)

Base = declarative_base()

#models

class Voluntario(Base):
    __tablename__ = 'voluntario'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    nombre = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    telefono = Column(String(255))
    fecha_registro = Column(String(255))
    comuna_id = Column(Integer, ForeignKey("comuna.id"))

class Region(Base):
    __tablename__ = "region"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)


class Comuna(Base):
    __tablename__ = "comuna"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)
    region_id = Column(Integer, ForeignKey("region.id"), nullable=False)

    region = relationship("Region")


class Ave(Base):
    __tablename__ = "ave"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(255), nullable=False)


class Avistamiento(Base):
    __tablename__ = "avistamiento"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    voluntario_id = Column(BigInteger, ForeignKey("voluntario.id"), nullable=False)
    ave_id = Column(Integer, ForeignKey("ave.id"), nullable=False)
    fecha_hora = Column(DateTime, nullable=False)
    lugar = Column(String(255), nullable=False)
    descripcion = Column(String(255))

    ave = relationship("Ave")


class Registro(Base):
    __tablename__ = "registro"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    ruta_archivo = Column(String(255), nullable=False)
    nombre_archivo = Column(String(255), nullable=False)
    avistamiento_id = Column(BigInteger, ForeignKey("avistamiento.id"), nullable=False)
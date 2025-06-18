# models/db_setup.py
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class ContaBancaria(Base):
    __tablename__ = 'contas'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    saldo = Column(Float)

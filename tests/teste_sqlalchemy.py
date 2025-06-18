# teste_sqlalchemy.py
from sqlalchemy import create_engine

engine = create_engine('sqlite:///:memory:')
print("SQLAlchemy importado com sucesso!")
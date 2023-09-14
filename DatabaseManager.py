from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from urllib.parse import quote_plus

senha = quote_plus('P@ssw0rd!')
engine = create_engine(f'mssql+pyodbc://sa:{senha}@localhost/Dados?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes')

_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from urllib.parse import quote_plus

senha = quote_plus('P@ssw0rd')
servidor = 'nameserver-prd.mysql.database.azure.com'
banco_de_dados = 'NameServer'
usuario = 'sadmin01'
porta = 3306

# Crie o URL de conexão para o MySQL na Azure
engine = create_engine(f"mysql+mysqlconnector://{usuario}:{senha}@{servidor}:{porta}/{banco_de_dados}")

# senha = quote_plus('P@ssw0rd!')
# engine = create_engine(f'mssql+pyodbc://sa:{senha}@localhost/Dados?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes')

_SessionFactory = sessionmaker(bind=engine)

Base = declarative_base()

def session_factory():
    Base.metadata.create_all(engine)
    return _SessionFactory()

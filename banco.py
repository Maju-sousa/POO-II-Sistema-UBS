import os

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Dados de conexão com o PostgreSQL que roda dentro do container Docker
# (ver docker-compose.yml). Usamos variáveis de ambiente com valores
# padrão para não precisar reescrever o código se alguma credencial
# mudar.
DB_USER = os.getenv("DB_USER", "ubs_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "ubs_senha")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5433")
DB_NAME = os.getenv("DB_NAME", "ubs_db")

# Usamos o driver "psycopg" (versão 3), e não o "psycopg2". O psycopg2
# usa a biblioteca C libpq, que em algumas instalações do Windows com
# locale pt-BR herda variáveis do sistema operacional decodificadas em
# CP1252/Latin-1 — e quebra com UnicodeDecodeError ao tentar interpretá-las
# como UTF-8. O psycopg (v3) é puro/mais robusto nesse aspecto e evita
# esse problema.
#
# A porta padrão 5433 (em vez da 5432 padrão do Postgres) é usada para
# não conflitar com uma instalação do PostgreSQL já existente direto no
# Windows, que normalmente ocupa a porta 5432.
DATABASE_URL = (
    f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)

Base = declarative_base()
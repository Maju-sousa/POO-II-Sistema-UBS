from sqlalchemy import Column, String, Integer
from banco import Base


class Paciente(Base):
    __tablename__ = "pacientes"

    cpf = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    nascimento = Column(String, nullable=False)
    telefone = Column(String, nullable=False)


class Profissional(Base):
    __tablename__ = "profissionais"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String, nullable=False)


class UBS(Base):
    __tablename__ = "ubs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)


class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, autoincrement=True)

    paciente_cpf = Column(String, nullable=False)
    profissional_nome = Column(String, nullable=False)
    ubs_nome = Column(String, nullable=False)

    data = Column(String, nullable=False)
    horario = Column(String, nullable=False)

    status = Column(String, default="Agendada")

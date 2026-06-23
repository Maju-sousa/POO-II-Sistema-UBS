from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from banco import Base


class Paciente(Base):
    __tablename__ = "pacientes"

    cpf = Column(String, primary_key=True)
    nome = Column(String, nullable=False)
    nascimento = Column(String, nullable=False)
    telefone = Column(String, nullable=False)

    consultas = relationship("Consulta", back_populates="paciente")


class Profissional(Base):
    __tablename__ = "profissionais"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String, nullable=False)

    consultas = relationship("Consulta", back_populates="profissional")


class UBS(Base):
    __tablename__ = "ubs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String, nullable=False)
    endereco = Column(String, nullable=False)

    consultas = relationship("Consulta", back_populates="ubs")


class Consulta(Base):
    __tablename__ = "consultas"

    id = Column(Integer, primary_key=True, autoincrement=True)

    # Chaves estrangeiras de verdade, em vez de guardar nome/texto.
    # Isso elimina dependência transitiva e redundância de dados,
    # mantendo a tabela em conformidade com a 3ª Forma Normal (3FN):
    # cada coluna não-chave depende apenas da chave primária, e não
    # de outra coluna não-chave (ex.: profissional_nome dependia
    # indiretamente do profissional, não da consulta em si).
    paciente_cpf = Column(String, ForeignKey("pacientes.cpf"), nullable=False)
    profissional_id = Column(Integer, ForeignKey("profissionais.id"), nullable=False)
    ubs_id = Column(Integer, ForeignKey("ubs.id"), nullable=False)

    data = Column(String, nullable=False)
    horario = Column(String, nullable=False)

    status = Column(String, default="Agendada")

    paciente = relationship("Paciente", back_populates="consultas")
    profissional = relationship("Profissional", back_populates="consultas")
    ubs = relationship("UBS", back_populates="consultas")

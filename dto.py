from dataclasses import dataclass


@dataclass
class Paciente:
    nome: str
    cpf: str
    nascimento: str
    telefone: str


@dataclass
class Profissional:
    nome: str
    especialidade: str


@dataclass
class UBS:
    nome: str
    endereco: str


@dataclass
class Consulta:
    paciente_cpf: str
    profissional_id: int
    ubs_id: int
    data: str
    horario: str
    status: str = "Agendada"
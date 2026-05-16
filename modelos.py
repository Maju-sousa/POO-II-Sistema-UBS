
class Paciente:
    def __init__(self, nome, cpf, nascimento, telefone):
        self.nome = nome
        self.cpf = cpf
        self.nascimento = nascimento
        self.telefone = telefone

    def to_dict(self): return self.__dict__

class Profissional:
    def __init__(self, nome, especialidade):
        self.nome = nome
        self.especialidade = especialidade

    def to_dict(self): return self.__dict__

class UBS:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def to_dict(self): return self.__dict__

class Consulta:
    def __init__(self, paciente_cpf, profissional_nome, ubs_nome, data, horario, status="Agendada"):
        self.paciente_cpf = paciente_cpf
        self.profissional_nome = profissional_nome
        self.ubs_nome = ubs_nome
        self.data = data        
        self.horario = horario  
        self.status = status    
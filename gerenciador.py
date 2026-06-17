import time

from banco import Session
from modelos import Paciente, Profissional, UBS, Consulta


class GerenciadorSistema:

    def __init__(self):

        self.session = Session()

        self.dados = {
            "pacientes": [],
            "profissionais": [],
            "ubs": [],
            "consultas": []
        }

        self.carregar_dados()

    def carregar_dados(self):

        self.dados["pacientes"] = [
            {
                "cpf": p.cpf,
                "nome": p.nome,
                "nascimento": p.nascimento,
                "telefone": p.telefone
            }
            for p in self.session.query(Paciente).all()
        ]

        self.dados["profissionais"] = [
            {
                "nome": p.nome,
                "especialidade": p.especialidade
            }
            for p in self.session.query(Profissional).all()
        ]

        self.dados["ubs"] = [
            {
                "nome": u.nome,
                "endereco": u.endereco
            }
            for u in self.session.query(UBS).all()
        ]

        self.dados["consultas"] = [
            {
                "paciente_cpf": c.paciente_cpf,
                "profissional_nome": c.profissional_nome,
                "ubs_nome": c.ubs_nome,
                "data": c.data,
                "horario": c.horario,
                "status": c.status
            }
            for c in self.session.query(Consulta).all()
        ]

    def salvar_dados(self):

        yield 25
        time.sleep(0.1)

        self.session.commit()

        yield 100

    def adicionar_paciente(self, p):

        paciente = Paciente(
            cpf=p.cpf,
            nome=p.nome,
            nascimento=p.nascimento,
            telefone=p.telefone
        )

        self.session.add(paciente)
        self.session.commit()

        self.carregar_dados()

    def adicionar_profissional(self, pr):

        profissional = Profissional(
            nome=pr.nome,
            especialidade=pr.especialidade
        )

        self.session.add(profissional)
        self.session.commit()

        self.carregar_dados()

    def adicionar_ubs(self, u):

        unidade = UBS(
            nome=u.nome,
            endereco=u.endereco
        )

        self.session.add(unidade)
        self.session.commit()

        self.carregar_dados()

    def agendar_consulta(self, c):

        consulta_existente = (
            self.session.query(Consulta)
            .filter(
                Consulta.profissional_nome == c.profissional_nome,
                Consulta.data == c.data,
                Consulta.horario == c.horario,
                Consulta.status == "Agendada"
            )
            .first()
        )

        if consulta_existente:
            raise ValueError(
                f"O médico {c.profissional_nome} já possui consulta neste horário!"
            )

        consulta = Consulta(
            paciente_cpf=c.paciente_cpf,
            profissional_nome=c.profissional_nome,
            ubs_nome=c.ubs_nome,
            data=c.data,
            horario=c.horario,
            status=c.status
        )

        self.session.add(consulta)
        self.session.commit()

        self.carregar_dados()

    def alterar_status_consulta(
        self,
        paciente_cpf,
        data,
        horario,
        novo_status
    ):

        consulta = (
            self.session.query(Consulta)
            .filter(
                Consulta.paciente_cpf == paciente_cpf,
                Consulta.data == data,
                Consulta.horario == horario
            )
            .first()
        )

        if consulta:

            consulta.status = novo_status

            self.session.commit()

            self.carregar_dados()

    def obter_contadores(self):

        consultas_ativas = (
            self.session.query(Consulta)
            .filter(
                Consulta.status == "Agendada"
            )
            .count()
        )

        return {
            "pacientes": self.session.query(Paciente).count(),
            "profissionais": self.session.query(Profissional).count(),
            "ubs": self.session.query(UBS).count(),
            "consultas": consultas_ativas
        }

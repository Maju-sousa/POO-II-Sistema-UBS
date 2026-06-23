import time

from banco import Session
from modelos import Paciente, Profissional, UBS, Consulta


class GerenciadorSistema:

    def __init__(self):

        self.dados = {
            "pacientes": [],
            "profissionais": [],
            "ubs": [],
            "consultas": []
        }

        self.carregar_dados()

    def carregar_dados(self):

        with Session() as session:

            self.dados["pacientes"] = [
                {
                    "cpf": p.cpf,
                    "nome": p.nome,
                    "nascimento": p.nascimento,
                    "telefone": p.telefone
                }
                for p in session.query(Paciente).all()
            ]

            self.dados["profissionais"] = [
                {
                    "id": p.id,
                    "nome": p.nome,
                    "especialidade": p.especialidade
                }
                for p in session.query(Profissional).all()
            ]

            self.dados["ubs"] = [
                {
                    "id": u.id,
                    "nome": u.nome,
                    "endereco": u.endereco
                }
                for u in session.query(UBS).all()
            ]

            self.dados["consultas"] = [
                {
                    "paciente_cpf": c.paciente_cpf,
                    "profissional_id": c.profissional_id,
                    "profissional_nome": c.profissional.nome,
                    "ubs_id": c.ubs_id,
                    "ubs_nome": c.ubs.nome,
                    "data": c.data,
                    "horario": c.horario,
                    "status": c.status
                }
                for c in session.query(Consulta).all()
            ]

    def salvar_dados(self):
        # Mantido apenas para preservar a barra de progresso na thread.
        # O commit real de cada operação já acontece dentro do método
        # correspondente (adicionar_paciente, agendar_consulta, etc).
        yield 25
        time.sleep(0.1)
        yield 100

    def adicionar_paciente(self, p):

        with Session() as session:

            paciente = Paciente(
                cpf=p.cpf,
                nome=p.nome,
                nascimento=p.nascimento,
                telefone=p.telefone
            )

            session.add(paciente)
            session.commit()

        self.carregar_dados()

    def adicionar_profissional(self, pr):

        with Session() as session:

            profissional = Profissional(
                nome=pr.nome,
                especialidade=pr.especialidade
            )

            session.add(profissional)
            session.commit()

        self.carregar_dados()

    def adicionar_ubs(self, u):

        with Session() as session:

            unidade = UBS(
                nome=u.nome,
                endereco=u.endereco
            )

            session.add(unidade)
            session.commit()

        self.carregar_dados()

    def agendar_consulta(self, c):

        with Session() as session:

            consulta_existente = (
                session.query(Consulta)
                .filter(
                    Consulta.profissional_id == c.profissional_id,
                    Consulta.data == c.data,
                    Consulta.horario == c.horario,
                    Consulta.status == "Agendada"
                )
                .first()
            )

            if consulta_existente:
                raise ValueError(
                    "Este profissional já possui consulta neste horário!"
                )

            consulta = Consulta(
                paciente_cpf=c.paciente_cpf,
                profissional_id=c.profissional_id,
                ubs_id=c.ubs_id,
                data=c.data,
                horario=c.horario,
                status=c.status
            )

            session.add(consulta)
            session.commit()

        self.carregar_dados()

    def alterar_status_consulta(
        self,
        paciente_cpf,
        data,
        horario,
        novo_status
    ):

        with Session() as session:

            consulta = (
                session.query(Consulta)
                .filter(
                    Consulta.paciente_cpf == paciente_cpf,
                    Consulta.data == data,
                    Consulta.horario == horario
                )
                .first()
            )

            if consulta:
                consulta.status = novo_status
                session.commit()

        self.carregar_dados()

    def obter_contadores(self):

        with Session() as session:

            consultas_ativas = (
                session.query(Consulta)
                .filter(
                    Consulta.status == "Agendada"
                )
                .count()
            )

            return {
                "pacientes": session.query(Paciente).count(),
                "profissionais": session.query(Profissional).count(),
                "ubs": session.query(UBS).count(),
                "consultas": consultas_ativas
            }

from blinker import Signal
import requests

BASE_URL = "http://localhost:5000"


class ClienteAPI:
    """
    Substitui o GerenciadorSistema do ponto de vista da interface.
    Em vez de acessar o banco diretamente, faz requisições HTTP para a
    API Flask (api.py), que é quem de fato fala com o PostgreSQL.
    """

    def __init__(self):

        self.dados = {
            "pacientes": [],
            "profissionais": [],
            "ubs": [],
            "consultas": []
        }

    #    self.carregar_dados()

    def carregar_dados(self):

        self.dados["pacientes"] = requests.get(
            f"{BASE_URL}/pacientes"
        ).json()

        self.dados["profissionais"] = requests.get(
            f"{BASE_URL}/profissionais"
        ).json()

        self.dados["ubs"] = requests.get(
            f"{BASE_URL}/ubs"
        ).json()

        self.dados["consultas"] = requests.get(
            f"{BASE_URL}/consultas"
        ).json()

    def salvar_dados(self):
        yield 50
        yield 100


    def _verificar_resposta(self, resposta):
        corpo = resposta.json()

        if not corpo.get("sucesso", True):
            raise ValueError(corpo.get("erro", "Erro desconhecido na API."))

        if not resposta.ok:
            raise ValueError(f"Erro na API (HTTP {resposta.status_code}).")

    def adicionar_paciente(self, p):

        resposta = requests.post(
            f"{BASE_URL}/pacientes",
            json={
                "cpf": p.cpf,
                "nome": p.nome,
                "nascimento": p.nascimento,
                "telefone": p.telefone
            }
        )

        self._verificar_resposta(resposta)
        self.carregar_dados()

    def adicionar_profissional(self, pr):

        resposta = requests.post(
            f"{BASE_URL}/profissionais",
            json={
                "nome": pr.nome,
                "especialidade": pr.especialidade
            }
        )

        self._verificar_resposta(resposta)
        self.carregar_dados()

    def adicionar_ubs(self, u):

        resposta = requests.post(
            f"{BASE_URL}/ubs",
            json={
                "nome": u.nome,
                "endereco": u.endereco
            }
        )

        self._verificar_resposta(resposta)
        self.carregar_dados()

    def agendar_consulta(self, c):

        resposta = requests.post(
            f"{BASE_URL}/consultas",
            json={
                "paciente_cpf": c.paciente_cpf,
                "profissional_id": c.profissional_id,
                "ubs_id": c.ubs_id,
                "data": c.data,
                "horario": c.horario,
                "status": c.status
            }
        )

        self._verificar_resposta(resposta)
        self.carregar_dados()

    def alterar_status_consulta(self, paciente_cpf, data, horario, novo_status):

        resposta = requests.put(
            f"{BASE_URL}/consultas/status",
            json={
                "paciente_cpf": paciente_cpf,
                "data": data,
                "horario": horario,
                "novo_status": novo_status
            }
        )

        self._verificar_resposta(resposta)
        self.carregar_dados()

    def obter_contadores(self):
        # Conta os dados locais que já foram carregados pela thread
        consultas_ativas = sum(1 for c in self.dados["consultas"] if c.get("status") == "Agendada")
        
        return {
            "pacientes": len(self.dados["pacientes"]),
            "profissionais": len(self.dados["profissionais"]),
            "ubs": len(self.dados["ubs"]),
            "consultas": consultas_ativas
        }
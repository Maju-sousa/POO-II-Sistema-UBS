
import json
import os
import time

class GerenciadorSistema:
    def __init__(self):
        self.arquivo = "dados_sistema.json"
        self.dados = {"pacientes": [], "profissionais": [], "ubs": [], "consultas": []}
        self.carregar_dados()

    def carregar_dados(self):
        if os.path.exists(self.arquivo):
            try:
                with open(self.arquivo, 'r', encoding='utf-8') as f:
                    self.dados = json.load(f)
            except:
                pass

    def salvar_dados(self):
        yield 25
        time.sleep(0.1) 
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(self.dados, f, indent=4, ensure_ascii=False)
        yield 100

    def adicionar_paciente(self, p): self.dados["pacientes"].append(p.to_dict())
    def adicionar_profissional(self, pr): self.dados["profissionais"].append(pr.to_dict())
    def adicionar_ubs(self, u): self.dados["ubs"].append(u.to_dict())
    
    def agendar_consulta(self, c):
        
        for consulta in self.dados["consultas"]:
            if (consulta["profissional_nome"] == c.profissional_nome and 
                consulta["data"] == c.data and 
                consulta["horario"] == c.horario and 
                consulta["status"] == "Agendada"):
                raise ValueError(f"O médico {c.profissional_nome} já possui consulta neste horário!")
        self.dados["consultas"].append(c.__dict__)

    def alterar_status_consulta(self, paciente_cpf, data, horario, novo_status):
        for c in self.dados["consultas"]:
            if c["paciente_cpf"] == paciente_cpf and c["data"] == data and c["horario"] == horario:
                c["status"] = novo_status
                break

    def obter_contadores(self):
        consultas_ativas = sum(1 for c in self.dados["consultas"] if c["status"] == "Agendada")
        return {
            "pacientes": len(self.dados["pacientes"]),
            "profissionais": len(self.dados["profissionais"]),
            "ubs": len(self.dados["ubs"]),
            "consultas": consultas_ativas
        }

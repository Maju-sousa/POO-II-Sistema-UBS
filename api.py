from flask import Flask, jsonify, request

from gerenciador import GerenciadorSistema
from modelos import Paciente, Profissional, UBS, Consulta

app = Flask(__name__)

gerenciador = GerenciadorSistema()


# ---------- PACIENTES ----------

@app.route("/pacientes", methods=["GET"])
def listar_pacientes():
    return jsonify(gerenciador.dados["pacientes"])


@app.route("/pacientes", methods=["POST"])
def criar_paciente():
    dados = request.get_json()

    paciente = Paciente(
        cpf=dados["cpf"],
        nome=dados["nome"],
        nascimento=dados["nascimento"],
        telefone=dados["telefone"]
    )

    try:
        gerenciador.adicionar_paciente(paciente)
        return jsonify({"sucesso": True}), 201
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 400


# ---------- PROFISSIONAIS ----------

@app.route("/profissionais", methods=["GET"])
def listar_profissionais():
    return jsonify(gerenciador.dados["profissionais"])


@app.route("/profissionais", methods=["POST"])
def criar_profissional():
    dados = request.get_json()

    profissional = Profissional(
        nome=dados["nome"],
        especialidade=dados["especialidade"]
    )

    try:
        gerenciador.adicionar_profissional(profissional)
        return jsonify({"sucesso": True}), 201
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 400


# ---------- UBS ----------

@app.route("/ubs", methods=["GET"])
def listar_ubs():
    return jsonify(gerenciador.dados["ubs"])


@app.route("/ubs", methods=["POST"])
def criar_ubs():
    dados = request.get_json()

    unidade = UBS(
        nome=dados["nome"],
        endereco=dados["endereco"]
    )

    try:
        gerenciador.adicionar_ubs(unidade)
        return jsonify({"sucesso": True}), 201
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 400


# ---------- CONSULTAS ----------

@app.route("/consultas", methods=["GET"])
def listar_consultas():
    return jsonify(gerenciador.dados["consultas"])


@app.route("/consultas", methods=["POST"])
def criar_consulta():
    dados = request.get_json()

    consulta = Consulta(
        paciente_cpf=dados["paciente_cpf"],
        profissional_id=dados["profissional_id"],
        ubs_id=dados["ubs_id"],
        data=dados["data"],
        horario=dados["horario"],
        status=dados.get("status", "Agendada")
    )

    try:
        gerenciador.agendar_consulta(consulta)
        return jsonify({"sucesso": True}), 201
    except ValueError as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 409
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 400


@app.route("/consultas/status", methods=["PUT"])
def alterar_status_consulta():
    dados = request.get_json()

    try:
        gerenciador.alterar_status_consulta(
            dados["paciente_cpf"],
            dados["data"],
            dados["horario"],
            dados["novo_status"]
        )
        return jsonify({"sucesso": True})
    except Exception as e:
        return jsonify({"sucesso": False, "erro": str(e)}), 400


# ---------- CONTADORES (dashboard) ----------

@app.route("/contadores", methods=["GET"])
def obter_contadores():
    return jsonify(gerenciador.obter_contadores())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
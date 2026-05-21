from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QFormLayout, QFrame,
    QComboBox, QDateEdit, QTimeEdit, QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt, QDate, QTime, Signal
from PySide6.QtGui import QColor

from PySide6.QtWidgets import QHBoxLayout

class CardIndicador(QFrame):
    def __init__(self, titulo, valor, icone="👤", cor="#6366F1"):
        super().__init__()

        self.setObjectName("CardIndicador")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(8)

        # 🔹 TOPO (titulo + icone)
        topo = QHBoxLayout()

        self.lbl_titulo = QLabel(titulo)
        self.lbl_titulo.setStyleSheet("color: #64748B; font-size: 13px;")

        self.lbl_icone = QLabel(icone)
        self.lbl_icone.setStyleSheet(f"""
            font-size: 18px;
            background-color: {cor}22;
            padding: 6px;
            border-radius: 8px;
        """)

        topo.addWidget(self.lbl_titulo)
        topo.addStretch()
        topo.addWidget(self.lbl_icone)

        # 🔹 VALOR
        self.lbl_valor = QLabel(str(valor))
        self.lbl_valor.setStyleSheet("font-size: 28px; font-weight: bold; color:#0F172A;")

        layout.addLayout(topo)
        layout.addWidget(self.lbl_valor)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(25)
        shadow.setOffset(0, 6)
        shadow.setColor(QColor(0, 0, 0, 40))
        self.setGraphicsEffect(shadow)

class CardGenerico(QFrame):
    def __init__(self, titulo, dados):
        super().__init__()

        self.setObjectName("CardDado")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(6)

        lbl_titulo = QLabel(titulo)
        lbl_titulo.setStyleSheet("font-size: 15px; font-weight: bold; color:#0F172A;")
        layout.addWidget(lbl_titulo)

        for k, v in dados.items():
            lbl = QLabel(f"<b>{k}:</b> {v}")
            lbl.setStyleSheet("color: #475569; font-size: 12px;")
            layout.addWidget(lbl)

        # SOMBRA
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(0, 0, 0, 30))
        self.setGraphicsEffect(shadow)


# =========================
# CARD CONSULTA
# =========================
class CardConsulta(QFrame):
    cancelar_clicked = Signal()

    def __init__(self, nome_p, cpf, medico, ubs, data, hora, status):
        super().__init__()

        self.setObjectName("CardDado")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(6)

        header = QHBoxLayout()

        lbl_nome = QLabel(nome_p)
        lbl_nome.setStyleSheet("font-size: 15px; font-weight: bold; color:#0F172A;")

        btn_cancelar = QPushButton("✕")
        btn_cancelar.setFixedSize(20, 20)
        btn_cancelar.setStyleSheet("color:#EF4444; border:none; background:transparent;")
        btn_cancelar.clicked.connect(self.cancelar_clicked.emit)

        if status != "Agendada":
            btn_cancelar.hide()

        header.addWidget(lbl_nome)
        header.addStretch()
        header.addWidget(btn_cancelar)

        layout.addLayout(header)

        layout.addWidget(QLabel(f"<span style='color:#64748B;'>CPF:</span> {cpf}"))
        layout.addWidget(QLabel(f"<b>Profissional:</b> {medico}"))
        layout.addWidget(QLabel(f"<b>UBS:</b> {ubs}"))

        footer = QHBoxLayout()
        footer.addWidget(QLabel(f"📅 {data}  🕒 {hora}"))

        badge = QLabel(status)
        cor = "#10B981" if status == "Agendada" else "#EF4444"
        badge.setStyleSheet(f"""
            background-color: {cor}22;
            color: {cor};
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: bold;
        """)

        footer.addStretch()
        footer.addWidget(badge)

        layout.addLayout(footer)

        # SOMBRA
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(0, 0, 0, 30))
        self.setGraphicsEffect(shadow)



class ModalBase(QDialog):
    def __init__(self, titulo, pai=None):
        super().__init__(pai)

        self.setWindowTitle(titulo)
        self.setMinimumWidth(380)

        layout = QVBoxLayout(self)

        lbl = QLabel(titulo)
        lbl.setStyleSheet("""
        font-size: 18px;
        font-weight: bold;
        color: white;
        """)
        layout.addWidget(lbl)

        self.form_layout = QFormLayout()
        layout.addLayout(self.form_layout)

        botoes = QHBoxLayout()

        btn_cancelar = QPushButton("Cancelar")
        btn_ok = QPushButton("Salvar")
        btn_ok.setObjectName("BtnAcaoPrincipal")

        btn_cancelar.clicked.connect(self.reject)
        btn_ok.clicked.connect(self.accept)

        botoes.addStretch()
        botoes.addWidget(btn_cancelar)
        botoes.addWidget(btn_ok)

        layout.addLayout(botoes)


class ModalPaciente(ModalBase):
    def __init__(self, pai=None):
        super().__init__("Paciente", pai)

        self.txt_nome = QLineEdit()
        self.txt_cpf = QLineEdit()
        self.txt_nasc = QLineEdit()
        self.txt_tel = QLineEdit()

        estilo_input = """
        QLineEdit{
            background-color: #1E293B;
            color: white;
            border: 1px solid #334155;
            border-radius: 10px;
            padding: 10px;
        }

        QLineEdit:focus{
            border: 2px solid #6366F1;
        }
        """

        # aplica o estilo nos inputs
        self.txt_nome.setStyleSheet(estilo_input)
        self.txt_cpf.setStyleSheet(estilo_input)
        self.txt_nasc.setStyleSheet(estilo_input)
        self.txt_tel.setStyleSheet(estilo_input)

        # labels
        lbl_nome = QLabel("Nome")
        lbl_nome.setStyleSheet("color: #E2E8F0; font-weight: bold;")

        lbl_cpf = QLabel("CPF")
        lbl_cpf.setStyleSheet("color: #E2E8F0; font-weight: bold;")

        lbl_nasc = QLabel("Nascimento")
        lbl_nasc.setStyleSheet("color: #E2E8F0; font-weight: bold;")

        lbl_tel = QLabel("Telefone")
        lbl_tel.setStyleSheet("color: #E2E8F0; font-weight: bold;")

        # adiciona no formulário
        self.form_layout.addRow(lbl_nome, self.txt_nome)
        self.form_layout.addRow(lbl_cpf, self.txt_cpf)
        self.form_layout.addRow(lbl_nasc, self.txt_nasc)
        self.form_layout.addRow(lbl_tel, self.txt_tel)

        


class ModalProfissional(ModalBase):
    def __init__(self, pai=None):
        super().__init__("Profissional", pai)
        self.txt_nome = QLineEdit()
        self.txt_espe = QLineEdit()

        self.form_layout.addRow("Nome", self.txt_nome)
        self.form_layout.addRow("Especialidade", self.txt_espe)


class ModalUBS(ModalBase):
    def __init__(self, pai=None):
        super().__init__("UBS", pai)
        self.txt_nome = QLineEdit()
        self.txt_end = QLineEdit()

        self.form_layout.addRow("Nome", self.txt_nome)
        self.form_layout.addRow("Endereço", self.txt_end)


class ModalConsulta(ModalBase):
    def __init__(self, pacientes, profissionais, ubs_list, pai=None):
        super().__init__("Consulta", pai)

        self.cb_p = QComboBox()
        for p in pacientes:
            self.cb_p.addItem(p["nome"], p["cpf"])

        self.cb_pr = QComboBox()
        for pr in profissionais:
            self.cb_pr.addItem(pr["nome"], pr["nome"])

        self.cb_u = QComboBox()
        for u in ubs_list:
            self.cb_u.addItem(u["nome"], u["nome"])

        self.date_edit = QDateEdit(QDate.currentDate())
        self.time_edit = QTimeEdit(QTime.currentTime())

        self.form_layout.addRow("Paciente", self.cb_p)
        self.form_layout.addRow("Profissional", self.cb_pr)
        self.form_layout.addRow("UBS", self.cb_u)
        self.form_layout.addRow("Data", self.date_edit)
        self.form_layout.addRow("Hora", self.time_edit)

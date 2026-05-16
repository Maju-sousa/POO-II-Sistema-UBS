from PySide6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QFormLayout, QFrame, QComboBox, QDateEdit, QTimeEdit)
from PySide6.QtCore import Qt, QDate, QTime, Signal
from interface.estilos import ESTILO_COMPONENTES

class CardIndicador(QFrame):
    def __init__(self, titulo, valor_inicial, cor_icone="#2563EB"):
        super().__init__()
        self.setObjectName("CardIndicador")
        self.setStyleSheet(ESTILO_COMPONENTES)
        self.setFixedSize(220, 130)
        
        layout = QVBoxLayout(self)
        
        top_layout = QHBoxLayout()
        lbl_titulo = QLabel(titulo)
        lbl_titulo.setStyleSheet("font-size: 13px; color: #64748B; font-weight: 500;")
        lbl_icon = QLabel("📊") # Pode trocar por QPixmap se quiser usar imagens reais
        lbl_icon.setStyleSheet(f"font-size: 16px; background-color: {cor_icone}22; padding: 4px; border-radius: 8px;")
        top_layout.addWidget(lbl_titulo)
        top_layout.addStretch()
        top_layout.addWidget(lbl_icon)
        
        self.lbl_valor = QLabel(str(valor_inicial))
        self.lbl_valor.setStyleSheet("font-size: 32px; font-weight: bold; color: #0F172A; margin-top: 10px;")
        
        layout.addLayout(top_layout)
        layout.addWidget(self.lbl_valor)

class CardGenerico(QFrame):
    def __init__(self, titulo, dicionario_dados):
        super().__init__()
        self.setObjectName("CardDado")
        self.setStyleSheet(ESTILO_COMPONENTES)
        self.setMinimumWidth(260)
        
        layout = QVBoxLayout(self)
        
        lbl_titulo = QLabel(titulo)
        lbl_titulo.setStyleSheet("font-size: 16px; font-weight: bold; color: #0F172A;")
        layout.addWidget(lbl_titulo)
        
        for chave, valor in dicionario_dados.items():
            lbl_item = QLabel(f"<b>{chave}:</b> {valor}")
            lbl_item.setStyleSheet("font-size: 12px; color: #475569;")
            layout.addWidget(lbl_item)

class CardConsulta(QFrame):
    cancelar_clicked = Signal()

    def __init__(self, nome_p, cpf, medico, ubs, data, hora, status):
        super().__init__()
        self.setObjectName("CardDado")
        self.setStyleSheet(ESTILO_COMPONENTES)
        
        layout = QVBoxLayout(self)
        
        header = QHBoxLayout()
        lbl_nome = QLabel(nome_p)
        lbl_nome.setStyleSheet("font-size: 15px; font-weight: bold; color: #0F172A;")
        
        btn_cancelar = QPushButton("✕")
        btn_cancelar.setFixedSize(20, 20)
        btn_cancelar.setStyleSheet("color: #EF4444; border: none; font-weight: bold; background: transparent;")
        btn_cancelar.clicked.connect(self.cancelar_clicked.emit)
        if status != "Agendada": btn_cancelar.hide()
        
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
        cor_b = "#10B981" if status == "Agendada" else "#EF4444"
        badge.setStyleSheet(f"background-color: {cor_b}22; color: {cor_b}; padding: 3px 8px; border-radius: 6px; font-weight: bold; font-size: 11px;")
        footer.addStretch()
        footer.addWidget(badge)
        layout.addLayout(footer)

class ModalBase(QDialog):
    def __init__(self, titulo, pai=None):
        super().__init__(pai)
        self.setWindowTitle(titulo)
        self.setStyleSheet(ESTILO_COMPONENTES)
        self.setWindowModality(Qt.ApplicationModal)
        self.setMinimumWidth(380)
        
        self.layout_principal = QVBoxLayout(self)
        lbl_chamada = QLabel(titulo)
        lbl_chamada.setStyleSheet("font-size: 18px; font-weight: bold; color: #0F172A; margin-bottom: 10px;")
        self.layout_principal.addWidget(lbl_chamada)
        
        self.form_layout = QFormLayout()
        self.layout_principal.addLayout(self.form_layout)
        
        botoes = QHBoxLayout()
        self.btn_cancelar = QPushButton("Cancelar")
        self.btn_cancelar.setStyleSheet("background: white; border: 1px solid #CBD5E1; border-radius: 8px; padding: 8px;")
        self.btn_cadastrar = QPushButton("Cadastrar")
        self.btn_cadastrar.setObjectName("BtnAcaoPrincipal")
        
        self.btn_cancelar.clicked.connect(self.reject)
        self.btn_cadastrar.clicked.connect(self.accept)
        
        botoes.addStretch()
        botoes.addWidget(self.btn_cancelar)
        botoes.addWidget(self.btn_cadastrar)
        self.layout_principal.addLayout(botoes)

class ModalPaciente(ModalBase):
    def __init__(self, pai=None):
        super().__init__("Cadastrar Paciente", pai)
        self.txt_nome = QLineEdit()
        self.txt_cpf = QLineEdit()
        self.txt_nasc = QLineEdit()
        self.txt_tel = QLineEdit()
        self.form_layout.addRow("Nome Completo", self.txt_nome)
        self.form_layout.addRow("CPF", self.txt_cpf)
        self.form_layout.addRow("Data de Nascimento", self.txt_nasc)
        self.form_layout.addRow("Telefone", self.txt_tel)

class ModalProfissional(ModalBase):
    def __init__(self, pai=None):
        super().__init__("Cadastrar Profissional", pai)
        self.txt_nome = QLineEdit()
        self.txt_espe = QLineEdit()
        self.form_layout.addRow("Nome Completo", self.txt_nome)
        self.form_layout.addRow("Especialidade", self.txt_espe)

class ModalUBS(ModalBase):
    def __init__(self, pai=None):
        super().__init__("Cadastrar UBS", pai)
        self.txt_nome = QLineEdit()
        self.txt_end = QLineEdit()
        self.form_layout.addRow("Nome da UBS", self.txt_nome)
        self.form_layout.addRow("Endereço", self.txt_end)

class ModalConsulta(ModalBase):
    def __init__(self, pacientes, profissionais, ubs_list, pai=None):
        super().__init__("Agendar Consulta", pai)
        self.btn_cadastrar.setText("Agendar")
        
        self.cb_p = QComboBox()
        for p in pacientes: self.cb_p.addItem(f"{p['nome']} - {p['cpf']}", p['cpf'])
        self.cb_pr = QComboBox()
        for pr in profissionais: self.cb_pr.addItem(pr['nome'], pr['nome'])
        self.cb_u = QComboBox()
        for u in ubs_list: self.cb_u.addItem(u['nome'], u['nome'])
        
        self.date_edit = QDateEdit(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)
        self.time_edit = QTimeEdit(QTime.currentTime())
        
        self.form_layout.addRow("Paciente", self.cb_p)
        self.form_layout.addRow("Profissional", self.cb_pr)
        self.form_layout.addRow("UBS", self.cb_u)
        self.form_layout.addRow("Data", self.date_edit)
        self.form_layout.addRow("Horário", self.time_edit)
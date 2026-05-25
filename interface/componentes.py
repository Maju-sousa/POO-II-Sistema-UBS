import qtawesome as qta
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QGridLayout, QFrame,
    QComboBox, QDateEdit, QTimeEdit, QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt, QDate, QTime, Signal
from PySide6.QtGui import QColor

class CampoMascarado(QLineEdit):
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        # aqui Verifica se há algum dígito preenchido; se não, move para o início
        if not any(c.isdigit() for c in self.text()):
            self.setCursorPosition(0)

class CardIndicador(QFrame):
    def __init__(self, titulo, valor, icone="👤", cor="#29227C"):
        super().__init__()
        self.setObjectName("CardIndicador")

        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 22, 22, 22)
        layout.setSpacing(12)

      
        topo = QHBoxLayout()

        self.lbl_titulo = QLabel(titulo)
        self.lbl_titulo.setStyleSheet("color: #64748B; font-size: 20px; font-weight: 500; background: transparent;")

        self.lbl_icone = QLabel(icone)
        
      
        self.lbl_icone = QLabel()
        
                        

        icone_qt = qta.icon(icone,color=cor)

        self.lbl_icone.setPixmap(icone_qt.pixmap(40, 40))

        self.lbl_icone.setAlignment(Qt.AlignCenter)

        self.lbl_icone.setFixedSize(42, 42)

        self.lbl_icone.setStyleSheet(f"""
         background-color: {cor}20;
         border-radius: 22px;
        """)
        

        topo.addWidget(self.lbl_titulo)
        topo.addStretch()
        topo.addWidget(self.lbl_icone)

        self.lbl_valor = QLabel(str(valor))
        self.lbl_valor.setStyleSheet("font-size: 28px; font-weight: bold; color: #1E293B; background: transparent;")

        layout.addLayout(topo)
        layout.addWidget(self.lbl_valor)

        
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(60)
        shadow.setOffset(0, 15)
        shadow.setColor(QColor(99, 102, 241, 18)) 
        self.setGraphicsEffect(shadow)

class CardGenerico(QFrame):
    def __init__(self, titulo, dados):
        super().__init__()
        self.setObjectName("CardDado")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(6)

        lbl_titulo = QLabel(titulo)
        lbl_titulo.setStyleSheet("font-size: 15px; font-weight: bold;")
        layout.addWidget(lbl_titulo)

        for k, v in dados.items():
            lbl = QLabel(f"<b>{k}:</b> {v}")
            lbl.setStyleSheet("color: #475569; font-size: 12px;")
            layout.addWidget(lbl)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(100)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(0, 0, 0, 15))
        self.setGraphicsEffect(shadow)


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
        lbl_nome.setStyleSheet("font-size: 15px; font-weight: bold;")

        btn_cancelar = QPushButton("✕")
        btn_cancelar.setFixedSize(20, 20)
        btn_cancelar.setCursor(Qt.PointingHandCursor)
        btn_cancelar.setStyleSheet("color:#EF4444; border:none; background:transparent; font-weight:bold;")
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
        footer.addWidget(QLabel(f"📅 {data}  &nbsp; 🕒 {hora}"))

        badge = QLabel(status)
        cor = "#10B981" if status == "Agendada" else "#EF4444"
        badge.setStyleSheet(f"""
            background-color: {cor}22;
            color: {cor};
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: bold;
        """)

        footer.addStretch()
        footer.addWidget(badge)
        layout.addLayout(footer)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(0, 5)
        shadow.setColor(QColor(0, 0, 0, 15))
        self.setGraphicsEffect(shadow)


class ModalBase(QDialog):
    def __init__(self, titulo, pai=None):
        super().__init__(pai)
        self.setWindowTitle(titulo)
        self.setMinimumWidth(400)
        
        
        self.setObjectName("ModalSistema") 

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        lbl = QLabel(f"Cadastrar {titulo}")
        lbl.setStyleSheet("font-size:18px; font-weight:bold; color: #1E293B;")
        layout.addWidget(lbl)

        self.form_layout = QGridLayout()
        self.form_layout.setColumnStretch(0, 0)  # Coluna 0 (labels) não expande
        self.form_layout.setColumnStretch(1, 1)  # Coluna 1 (campos) expande
        self.form_layout.setHorizontalSpacing(14)
        self.form_layout.setVerticalSpacing(14)
        self.form_row = 0  # Contador de linhas
        layout.addLayout(self.form_layout)

        botoes = QHBoxLayout()
        botoes.setSpacing(10)

        btn_cancelar = QPushButton("Cancelar")
        btn_cancelar.setCursor(Qt.PointingHandCursor)
        btn_cancelar.setStyleSheet("""
            QPushButton {
                background-color: #E2E8F0;
                color: #475569;
                border-radius: 10px;
                padding: 10px 18px;
                font-weight: bold;
            }
            QPushButton:hover { background-color: #CBD5E1; }
        """)
        
        btn_ok = QPushButton("Salvar")
        btn_ok.setObjectName("BtnAcaoPrincipal")
        btn_ok.setCursor(Qt.PointingHandCursor)

        btn_cancelar.clicked.connect(self.reject)
        btn_ok.clicked.connect(self.accept)

        botoes.addStretch()
        botoes.addWidget(btn_cancelar)
        botoes.addWidget(btn_ok)

        layout.addLayout(botoes)

    def addFormRow(self, label_text, widget):
        """Adiciona uma linha ao grid com label e widget"""
        lbl = QLabel(label_text)
        lbl.setStyleSheet("color: #1E293B; font-weight: 500;")
        self.form_layout.addWidget(lbl, self.form_row, 0)
        self.form_layout.addWidget(widget, self.form_row, 1)
        self.form_row += 1


class ModalPaciente(ModalBase):
    def __init__(self, pai=None):
        super().__init__("Paciente", pai)

        self.txt_nome = QLineEdit()
        self.txt_cpf = CampoMascarado()
        self.txt_nasc = CampoMascarado()
        self.txt_tel = CampoMascarado()

        self.txt_nome.setPlaceholderText("Nome completo")

        self.txt_cpf.setInputMask("000.000.000-00")
        self.txt_nasc.setInputMask("00/00/0000")
        self.txt_tel.setInputMask("(00) 00000-0000")

        self.txt_nome.setMaxLength(100)

        self.addFormRow("Nome Completo:", self.txt_nome)
        self.addFormRow("CPF:", self.txt_cpf)
        self.addFormRow("Nascimento:", self.txt_nasc)
        self.addFormRow("Telefone:", self.txt_tel)


class ModalProfissional(ModalBase):
    def __init__(self, pai=None):
        super().__init__("Profissional", pai)

        self.txt_nome = QLineEdit()
        self.txt_espe = QLineEdit()
        self.txt_crm = QLineEdit()

        
        self.txt_nome.setPlaceholderText("Nome")
        self.txt_espe.setPlaceholderText("Especialidade")
        self.txt_crm.setPlaceholderText("Ex: 123456-PI")

        
        self.txt_nome.setMaxLength(100)
        self.txt_espe.setMaxLength(50)
        self.txt_crm.setMaxLength(15)

        self.addFormRow("Nome do Profissional:", self.txt_nome)
        self.addFormRow("Especialidade:", self.txt_espe)
        self.addFormRow("CRM:", self.txt_crm)


class ModalUBS(ModalBase):
    def __init__(self, pai=None):
        super().__init__("UBS", pai)
        self.txt_nome = QLineEdit()
        self.txt_end = QLineEdit()

        self.addFormRow("Nome da Unidade:", self.txt_nome)
        self.addFormRow("Endereço:", self.txt_end)


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
        self.date_edit.setCalendarPopup(True) 
        self.time_edit = QTimeEdit(QTime.currentTime())

        self.time_edit.setDisplayFormat("HH:mm")
        self.date_edit.setDisplayFormat("dd/MM/yyyy")

        self.addFormRow("Paciente:", self.cb_p)
        self.addFormRow("Profissional:", self.cb_pr)
        self.addFormRow("UBS de Atendimento:", self.cb_u)
        self.addFormRow("Data da Consulta:", self.date_edit)
        self.addFormRow("Horário:", self.time_edit)

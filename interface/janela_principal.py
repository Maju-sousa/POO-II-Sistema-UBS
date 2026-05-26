import sys
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QStackedWidget, QLabel, QScrollArea,
    QGridLayout, QMessageBox, QProgressBar,
    QComboBox, QDateEdit, QFrame
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, Slot, QDate

from interface.estilos import (
    ESTILO_BARRA_LATERAL,
    ESTILO_GLOBAL,
    ESTILO_COMPONENTES
)

from interface.componentes import (
    CardIndicador,
    CardGenerico,
    CardConsulta,
    ModalPaciente,
    ModalProfissional,
    ModalUBS,
    ModalConsulta
)

from gerenciador import GerenciadorSistema
from modelos import Paciente, Profissional, UBS, Consulta
from threads import OperacaoArquivoWorker


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sistema de Agendamentos UBS")
        self.resize(1280, 760)

        self.setStyleSheet(
            ESTILO_GLOBAL +
            ESTILO_BARRA_LATERAL +
            ESTILO_COMPONENTES
        )

        self.gerenciador = GerenciadorSistema()

        self.init_ui()
        self.atualizar_todas_telas()

    def init_ui(self):

        layout_principal = QHBoxLayout()
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)

       



        self.barra_lateral = QFrame()
        self.barra_lateral.setObjectName("BarraLateral")
        self.barra_lateral.setFixedWidth(270)

        layout_menu = QVBoxLayout(self.barra_lateral)
        layout_menu.setContentsMargins(18, 25, 18, 25)
        layout_menu.setSpacing(14)

       
        avatar = QLabel()

        pixmap = QPixmap("assets/avatar.png")

        avatar.setPixmap(
          pixmap.scaled(
           95,
           95,
           Qt.KeepAspectRatio,
           Qt.SmoothTransformation
          )
        )

        avatar.setAlignment(Qt.AlignCenter)

        avatar.setStyleSheet("""
          padding: 8px;
          background-color: rgba(79,70,229,0.03);
          border-radius: 50px;
          """)

        lbl_titulo = QLabel("Sistema UBS")
        lbl_titulo.setObjectName("TituloApp")
        lbl_titulo.setAlignment(Qt.AlignCenter)

        subtitulo = QLabel("Painel Administrativo")
        subtitulo.setAlignment(Qt.AlignCenter)

        subtitulo.setStyleSheet("""
            color: #64748B;
            font-size: 12px;
            padding-bottom: 12px;
        """)

        linha = QFrame()
        linha.setFrameShape(QFrame.HLine)
        linha.setStyleSheet("""
            color: #E2E8F0;
            background: #E2E8F0;
            max-height: 1px;
        """)

        layout_menu.addWidget(avatar)
        layout_menu.addWidget(lbl_titulo)
        layout_menu.addWidget(subtitulo)
        layout_menu.addWidget(linha)
        layout_menu.addSpacing(10)


        self.botoes_menu = []

        abas = [
        ("⌂  Tela inicial", 0),
        ("◉  Pacientes", 1),
        ("✚  Profissionais", 2),
        ("▦   UBS", 3),
        ("◷  Agendamentos", 4)
     ]

        for texto, index in abas:

            btn = QPushButton(texto)

            btn.setObjectName("AbasMenu")
            btn.setCheckable(True)
            btn.setCursor(Qt.PointingHandCursor)

            if index == 0:
                btn.setChecked(True)

            btn.clicked.connect(
                lambda checked, idx=index:
                self.mudar_aba(idx)
            )

            layout_menu.addWidget(btn)
            self.botoes_menu.append(btn)

        layout_menu.addStretch()

        

        self.progress_bar = QProgressBar()
        self.progress_bar.setFixedHeight(8)
        self.progress_bar.setTextVisible(False)

        layout_menu.addWidget(self.progress_bar)

       

        self.paineis = QStackedWidget()

        self.setup_aba_dashboard()
        self.setup_aba_pacientes()
        self.setup_aba_profissionais()
        self.setup_aba_ubs()
        self.setup_aba_agendamentos()

        layout_principal.addWidget(self.barra_lateral)
        layout_principal.addWidget(self.paineis)

        container = QWidget()
        container.setLayout(layout_principal)

        self.setCentralWidget(container)

    

    def mudar_aba(self, idx):

        self.paineis.setCurrentIndex(idx)

        for i, btn in enumerate(self.botoes_menu):
            btn.setChecked(i == idx)

        self.atualizar_todas_telas()


    def setup_aba_dashboard(self):

        widget = QFrame()
        widget.setObjectName("Container")

        lay = QVBoxLayout(widget)

        lay.setContentsMargins(35, 35, 35, 35)
        lay.setSpacing(30)

        lbl = QLabel()

        lbl.setText("""
            <div>
                <span style='
                    font-size: 32px;
                    font-weight: 800;
                    color: #111827;
                '>
                    Painel Principal
                </span>

                <p style='
                    color:#64748B;
                    margin-top:6px;
                    font-size:14px;
                '>
                    Sistema de agendamentos
                </p>
            </div>
        """)

        lay.addWidget(lbl)

        self.grid_dash = QGridLayout()
        self.grid_dash.setSpacing(28)

        self.card_p = CardIndicador(
             "Pacientes",
             0,
             "fa5s.users",
            "#003B8E"
) 
        self.card_pr = CardIndicador(
             "Profissionais",
             0,
             "fa5s.stethoscope",
            "#003B8E"
)
        self.card_u = CardIndicador(
             "UBS",
             0,
             "fa5s.hospital",
             "#003B8E"
)
        self.card_c = CardIndicador(
            "Consultas",
            0,
            "fa5s.calendar-check",
            "#003B8E"
)

        self.grid_dash.addWidget(self.card_p, 0, 0)
        self.grid_dash.addWidget(self.card_pr, 0, 1)
        self.grid_dash.addWidget(self.card_u, 1, 0)
        self.grid_dash.addWidget(self.card_c, 1, 1)

        lay.addLayout(self.grid_dash)

       
        lay.addStretch()

        self.paineis.addWidget(widget)

    

    def criar_layout_cadastro(
        self,
        titulo,
        subtitulo,
        callback_novo
    ):

        widget = QFrame()
        widget.setObjectName("Container")

        lay = QVBoxLayout(widget)

        lay.setContentsMargins(35, 35, 35, 35)
        lay.setSpacing(28)

        topo = QHBoxLayout()

        lbl = QLabel()

        lbl.setText(f"""
            <div>
                <span style='
                    font-size: 30px;
                    font-weight: 800;
                    color: #111827;
                '>
                    {titulo}
                </span>

                <p style='
                    color:#64748B;
                    margin-top:6px;
                    font-size:14px;
                '>
                    {subtitulo}
                </p>
            </div>
        """)

        btn_novo = QPushButton(f"+ Novo")

        btn_novo.setObjectName("BtnAcaoPrincipal")
        btn_novo.setCursor(Qt.PointingHandCursor)

        btn_novo.clicked.connect(callback_novo)

        topo.addWidget(lbl)
        topo.addStretch()
        topo.addWidget(btn_novo)

        lay.addLayout(topo)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        conteudo_scroll = QWidget()
        conteudo_scroll.setObjectName("ConteudoScroll")

        grid = QGridLayout(conteudo_scroll)

        grid.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        grid.setSpacing(24)

        scroll.setWidget(conteudo_scroll)

        lay.addWidget(scroll)

        return widget, grid

    

    def setup_aba_pacientes(self):

        w, self.grid_pacientes = self.criar_layout_cadastro(
            "Pacientes",
            "Gerencie os pacientes cadastrados",
            self.abrir_modal_paciente
        )

        self.paineis.addWidget(w)

    

    def setup_aba_profissionais(self):

        w, self.grid_profissionais = self.criar_layout_cadastro(
            "Profissionais",
            "Gerencie os profissionais cadastrados",
            self.abrir_modal_profissional
        )

        self.paineis.addWidget(w)

    

    def setup_aba_ubs(self):

        w, self.grid_ubs = self.criar_layout_cadastro(
            "UBS",
            "Gerencie as unidades cadastradas",
            self.abrir_modal_ubs
        )

        self.paineis.addWidget(w)

    

    def setup_aba_agendamentos(self):

        widget = QFrame()
        widget.setObjectName("Container")

        lay = QVBoxLayout(widget)

        lay.setContentsMargins(35, 35, 35, 35)
        lay.setSpacing(28)

        topo = QHBoxLayout()

        lbl = QLabel()

        lbl.setText("""
            <div>
                <span style='
                    font-size: 30px;
                    font-weight: 800;
                    color: #111827;
                '>
                    Agendamentos
                </span>

                <p style='
                    color:#64748B;
                    margin-top:6px;
                    font-size:14px;
                '>
                    Gerenciamento de consultas
                </p>
            </div>
        """)

        btn_novo = QPushButton("+ Nova Consulta")

        btn_novo.setObjectName("BtnAcaoPrincipal")
        btn_novo.setCursor(Qt.PointingHandCursor)

        btn_novo.clicked.connect(self.abrir_modal_consulta)

        topo.addWidget(lbl)
        topo.addStretch()
        topo.addWidget(btn_novo)

        lay.addLayout(topo)

        
        filtros_layout = QHBoxLayout()
        filtros_layout.setSpacing(14)

        self.filtro_data = QDateEdit(QDate.currentDate())
        self.filtro_data.setCalendarPopup(True)

        self.filtro_data.dateChanged.connect(
            self.atualizar_tela_agendamentos
        )

        self.filtro_paciente = QComboBox()

        self.filtro_paciente.currentTextChanged.connect(
            self.atualizar_tela_agendamentos
        )

        filtros_layout.addWidget(QLabel("Data"))
        filtros_layout.addWidget(self.filtro_data)

        filtros_layout.addWidget(QLabel("Paciente"))
        filtros_layout.addWidget(self.filtro_paciente)

        filtros_layout.addStretch()

        lay.addLayout(filtros_layout)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        conteudo_scroll = QWidget()
        
        scroll.setStyleSheet("background: transparent; border: none;")
        conteudo_scroll.setStyleSheet("background: transparent;")

        self.grid_agendamentos = QGridLayout(conteudo_scroll)

        self.grid_agendamentos.setAlignment(
            Qt.AlignTop | Qt.AlignLeft
        )

        self.grid_agendamentos.setSpacing(24)

        scroll.setWidget(conteudo_scroll)

        lay.addWidget(scroll)

        self.paineis.addWidget(widget)

   

    def executar_operacao_async(self, acao, *args):

        self.progress_bar.setValue(0)

        self.worker = OperacaoArquivoWorker(
            self.gerenciador,
            acao,
            *args
        )

        self.worker.progresso.connect(
            self.progress_bar.setValue
        )

        self.worker.concluido.connect(
            self.finalizar_requisicao_async
        )

        self.worker.finished.connect(
            self.worker.deleteLater
        )

        self.worker.start()

    @Slot(bool, str)
    def finalizar_requisicao_async(self, sucesso, mensagem):

        if not sucesso:
            QMessageBox.critical(
                self,
                "Erro",
                mensagem
            )

        self.atualizar_todas_telas()
           

    def abrir_modal_paciente(self):

        m = ModalPaciente(self)

        if m.exec() == ModalPaciente.Accepted:

            p = Paciente(
                m.txt_nome.text(),
                m.txt_cpf.text(),
                m.txt_nasc.text(),
                m.txt_tel.text()
            )

            self.executar_operacao_async(
                self.gerenciador.adicionar_paciente,
                p
            )

    def abrir_modal_profissional(self):

        m = ModalProfissional(self)

        if m.exec() == ModalProfissional.Accepted:

            pr = Profissional(
                m.txt_nome.text(),
                m.txt_espe.text()
            )

            self.executar_operacao_async(
                self.gerenciador.adicionar_profissional,
                pr
            )

    def abrir_modal_ubs(self):

        m = ModalUBS(self)

        if m.exec() == ModalUBS.Accepted:

            u = UBS(
                m.txt_nome.text(),
                m.txt_end.text()
            )

            self.executar_operacao_async(
                self.gerenciador.adicionar_ubs,
                u
            )

    def abrir_modal_consulta(self):

        m = ModalConsulta(
            self.gerenciador.dados["pacientes"],
            self.gerenciador.dados["profissionais"],
            self.gerenciador.dados["ubs"],
            self
        )

        if m.exec() == ModalConsulta.Accepted:

            c = Consulta(
                m.cb_p.currentData(),
                m.cb_pr.currentText(),
                m.cb_u.currentText(),
                m.date_edit.date().toString("dd/MM/yyyy"),
                m.time_edit.time().toString("hh:mm")
            )

            self.executar_operacao_async(
                self.gerenciador.agendar_consulta,
                c
            )

    

    def limpar_grid(self, grid):

        while grid.count():

            item = grid.takeAt(0)

            if item.widget():
                item.widget().deleteLater()

    

    def atualizar_todas_telas(self):

        cont = self.gerenciador.obter_contadores()

        self.card_p.lbl_valor.setText(str(cont["pacientes"]))
        self.card_pr.lbl_valor.setText(str(cont["profissionais"]))
        self.card_u.lbl_valor.setText(str(cont["ubs"]))
        self.card_c.lbl_valor.setText(str(cont["consultas"]))

        

        self.limpar_grid(self.grid_pacientes)

        for i, p in enumerate(self.gerenciador.dados["pacientes"]):

            card = CardGenerico(
                p["nome"],
                {
                    "CPF": p["cpf"],
                    "Nascimento": p["nascimento"],
                    "Telefone": p["telefone"]
                }
            )

            self.grid_pacientes.addWidget(
                card,
                i // 2,
                i % 2
            )

       

        self.limpar_grid(self.grid_profissionais)

        for i, pr in enumerate(self.gerenciador.dados["profissionais"]):

            card = CardGenerico(
                pr["nome"],
                {
                    "Especialidade": pr["especialidade"]
                }
            )

            self.grid_profissionais.addWidget(
                card,
                i // 2,
                i % 2
            )

        

        self.limpar_grid(self.grid_ubs)

        for i, u in enumerate(self.gerenciador.dados["ubs"]):

            card = CardGenerico(
                u["nome"],
                {
                    "Endereço": u["endereco"]
                }
            )

            self.grid_ubs.addWidget(
                card,
                i // 2,
                i % 2
            )

        

        self.filtro_paciente.blockSignals(True)

        self.filtro_paciente.clear()

        self.filtro_paciente.addItem(
            "Todos os pacientes",
            "Todos"
        )

        for p in self.gerenciador.dados["pacientes"]:

            self.filtro_paciente.addItem(
                p["nome"],
                p["cpf"]
            )

        self.filtro_paciente.blockSignals(False)

        self.atualizar_tela_agendamentos()


    def atualizar_tela_agendamentos(self):

        self.limpar_grid(self.grid_agendamentos)

        data_filtro = self.filtro_data.date().toString("dd/MM/yyyy")

        paciente_filtro = self.filtro_paciente.currentData()

        consultas_filtradas = []

        for c in self.gerenciador.dados["consultas"]:

            if c["data"] != data_filtro:
                continue

            if (
                paciente_filtro != "Todos"
                and c["paciente_cpf"] != paciente_filtro
            ):
                continue

            consultas_filtradas.append(c)

        for i, c in enumerate(consultas_filtradas):

            nome_p = next(
                (
                    p["nome"]
                    for p in self.gerenciador.dados["pacientes"]
                    if p["cpf"] == c["paciente_cpf"]
                ),
                "Desconhecido"
            )

            card = CardConsulta(
                nome_p,
                c["paciente_cpf"],
                c["profissional_nome"],
                c["ubs_nome"],
                c["data"],
                c["horario"],
                c["status"]
            )

            card.cancelar_clicked.connect(
                lambda cp=c["paciente_cpf"],
                d=c["data"],
                h=c["horario"]:

                self.executar_operacao_async(
                    self.gerenciador.alterar_status_consulta,
                    cp,
                    d,
                    h,
                    "Cancelada"
                )
            )

            self.grid_agendamentos.addWidget(
                card,
                i // 2,
                i % 2
            )

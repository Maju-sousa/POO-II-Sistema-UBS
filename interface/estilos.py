ESTILO_GLOBAL = """
QMainWindow {
    background-color: qlineargradient(
        x1:0, y1:0,
        x2:1, y2:1,

        stop:0 #FFFFFF,
        stop:0.5 #F8FAFC,
        stop:1 #E0E7FF
    );
}

QFrame#Container {
    background: transparent;
}

QScrollArea {
    background: transparent;
    border: none;

}

QWidget#ConteudoScroll {
    background: transparent;
}

QDialog {
    background-color: rgba(255,255,255,0.98);
    border-radius: 24px;
}

QProgressBar {
    background-color: #E2E8F0;
    border-radius: 5px;
    height: 10px;
}

QProgressBar::chunk {
    background-color:#4338CA;
    border-radius: 5px;
}
"""


ESTILO_BARRA_LATERAL = """
QFrame#BarraLateral {

    background-color: rgba(255,255,255,0.96);

    border-right: 1px solid #E2E8F0;
}


/* =========================
   TÍTULO
========================= */

QLabel#TituloApp {

    font-size: 28px;

    font-weight: 800;

    color: #0F172A;

    padding-top: 10px;

    padding-bottom: 6px;

    font-family: 'Segoe UI';
}


/* =========================
   BOTÕES MENU
========================= */

QPushButton#AbasMenu {

    background-color: transparent;

    border: none;

    color: #475569;

    font-size: 15px;

    font-weight: 600;

    text-align: left;

    padding: 18px 22px;

    border-radius: 18px;

    font-family: 'Segoe UI';

    margin-top: 6px;
}


/* HOVER */

QPushButton#AbasMenu:hover {

    background-color: #EEF2FF;

    color: #312E81;
}


/* BOTÃO ATIVO */

QPushButton#AbasMenu:checked {

    background-color: #4F46E5;

    color: white;

    font-weight: 700;

    border-left: 5px solid #C7D2FE;
}


/* CLIQUE */

QPushButton#AbasMenu:pressed {

    background-color: #4338CA;
}
"""


ESTILO_COMPONENTES = """

/* =========================
   CARDS
========================= */

QFrame#CardIndicador,
QFrame#CardDado {

    background: qlineargradient(
        x1:0, y1:0,
        x2:1, y2:1,
        stop:0 #FFFFFF,
        stop:1 #F8FAFC
    );

    border: 1px solid #E2E8F0;

    border-radius: 30px;

    padding: 26px;
}


/* HOVER DOS CARDS */

QFrame#CardIndicador:hover,
QFrame#CardDado:hover {

    border: 1px solid #A5B4FC;

    background-color: #FFFFFF;
}


/* =========================
   BOTÃO PRINCIPAL
========================= */

QPushButton#BtnAcaoPrincipal {

    background-color: #4F46E5;

    color: white;

    font-size: 14px;

    font-weight: 700;

    border-radius: 16px;

    padding: 14px 26px;

    font-family: 'Segoe UI';
}

QPushButton#BtnAcaoPrincipal:hover {

    background-color: #4338CA;
}

QPushButton#BtnAcaoPrincipal:pressed {

    background-color: #3730A3;
}


/* =========================
   INPUTS
========================= */

QLineEdit,
QComboBox,
QDateEdit,
QTimeEdit {

    background-color: rgba(255,255,255,0.98);

    border: 1px solid #CBD5E1;

    border-radius: 14px;

    padding: 12px 16px;

    color: #334155;

    font-size: 14px;

    font-family: 'Segoe UI';
}

QLineEdit:focus,
QComboBox:focus,
QDateEdit:focus,
QTimeEdit:focus {

    border: 1px solid #6366F1;
}


/* =========================
   LABELS
========================= */

QLabel {

    color: #1E293B;

    font-family: 'Segoe UI';
}
"""

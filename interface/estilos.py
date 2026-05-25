ESTILO_GLOBAL = """
QMainWindow {
    background-color: #FFFFFF;
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
    background-color: #DCE7F2;
    border-radius: 5px;
    height: 10px;
}

QProgressBar::chunk {
    background-color: #003B8E;
    border-radius: 5px;
}
"""


ESTILO_BARRA_LATERAL = """
QFrame#BarraLateral {
    background-color: rgba(255,255,255,0.98);
    border-right: 1px solid #D6E4F0;
}

QLabel#TituloApp {
    font-size: 28px;
    font-weight: 800;
    color: #003B8E;
    padding-top: 10px;
    padding-bottom: 6px;
    font-family: 'Segoe UI';
}

QPushButton#AbasMenu {
    background-color: transparent;
    border: none;
    color: #003B8E;
    font-size: 15px;
    font-weight: 700;
    text-align: left;
    padding: 18px 22px;
    border-radius: 18px;
    font-family: 'Segoe UI';
    margin-top: 6px;
}

QPushButton#AbasMenu:hover {
    background-color: #E8F1FF;
    color: #0050C8;
}

QPushButton#AbasMenu:checked {
    background-color: #003B8E;
    color: white;
    font-weight: 700;
    border-left: 5px solid #0050C8;
}

QPushButton#AbasMenu:pressed {
    background-color: #002B6B;
}
"""


ESTILO_COMPONENTES = """
QFrame#CardIndicador,
QFrame#CardDado {
    background: #FFFFFF;
    border: 1px solid #D6E4F0;
    border-radius: 30px;
    padding: 26px;
}

QFrame#CardIndicador:hover,
QFrame#CardDado:hover {
    border: 1px solid #0050C8;
    background-color: #FFFFFF;
}

QPushButton#BtnAcaoPrincipal {
    background-color: #003B8E;
    color: white;
    font-size: 14px;
    font-weight: 700;
    border-radius: 16px;
    padding: 14px 26px;
    font-family: 'Segoe UI';
}

QPushButton#BtnAcaoPrincipal:hover {
    background-color: #0050C8;
}

QPushButton#BtnAcaoPrincipal:pressed {
    background-color: #002B6B;
}

QLineEdit,
QComboBox,
QDateEdit,
QTimeEdit {
    background-color: rgba(255,255,255,0.98);
    border: 1px solid #B7CADB;
    border-radius: 14px;
    padding: 12px 16px;
    color: #003B8E;
    font-size: 14px;
    font-family: 'Segoe UI';
}

QLineEdit:focus,
QComboBox:focus,
QDateEdit:focus,
QTimeEdit:focus {
    border: 1px solid #003B8E;
}

QLabel {
    color: #003B8E;
    font-family: 'Segoe UI';
}
"""
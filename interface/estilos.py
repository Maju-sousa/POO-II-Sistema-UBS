# interface/estilos.py

ESTILO_GLOBAL = """
QMainWindow {
    background-color: #F1F5F9;
}

QFrame#Container {
    background-color: #F1F5F9;
}

QScrollArea {
    background: transparent;
    border: none;
}

QWidget#ConteudoScroll {
    background: transparent;
}
"""

ESTILO_BARRA_LATERAL = """
QFrame#BarraLateral {
    background-color: #2D2F36;
    border-right: none;
}

/* Título */
QLabel#TituloApp {
    font-size: 18px;
    font-weight: bold;
    color: #FFFFFF;
    padding: 15px 10px;
    font-family: 'Segoe UI', Arial, sans-serif;
}

/* Botões do menu */
QPushButton#AbasMenu {
    background-color: transparent;
    border: none;
    color: #C0C0C0;
    font-size: 14px;
    text-align: left;
    padding: 12px 20px;
    border-radius: 8px;
    font-family: 'Segoe UI', Arial, sans-serif;
}

QPushButton#AbasMenu:hover {
    background-color: #3E4048;
    color: white;
}

QPushButton#AbasMenu:checked {
    background-color: #6C63FF;
    color: white;
    font-weight: bold;
}
"""


ESTILO_COMPONENTES = """
/* ===== CARDS ===== */
QFrame#CardIndicador, QFrame#CardDado {
    background-color: #FFFFFF;
    border-radius: 14px;
    padding: 18px;
}

/* Hover suave */
QFrame#CardDado:hover {
    background-color: #F8FAFC;
}

/* ===== BOTÃO PRINCIPAL ===== */
QPushButton#BtnAcaoPrincipal {
    background-color: #6366F1;
    color: white;
    font-size: 13px;
    font-weight: bold;
    border-radius: 10px;
    padding: 10px 18px;
}

QPushButton#BtnAcaoPrincipal:hover {
    background-color: #4F46E5;
}

/* ===== INPUTS ===== */
QLineEdit, QComboBox, QDateEdit, QTimeEdit {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 10px;
    padding: 8px 12px;
    color: #334155;
}

QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QTimeEdit:focus {
    border: 1px solid #6366F1;
}

/* ===== TEXTO ===== */
QLabel {
    color: #1E293B;
}
"""

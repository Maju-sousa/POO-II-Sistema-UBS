# interface/estilos.py

ESTILO_GLOBAL = """
QMainWindow {
    background-color: #F8FAFC;
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
    background-color: #FFFFFF;
    border-right: 1px solid #E2E8F0;
}
QLabel#TituloApp {
    font-size: 18px;
    font-weight: bold;
    color: #0F172A;
    padding: 15px 10px 5px 10px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton#AbasMenu {
    background-color: transparent;
    border: none;
    color: #64748B;
    font-size: 14px;
    text-align: left;
    padding: 12px 20px;
    border-radius: 8px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton#AbasMenu:checked {
    background-color: #EFF6FF;
    color: #2563EB;
    font-weight: bold;
}
QPushButton#AbasMenu:hover:!checked {
    background-color: #F1F5F9;
    color: #1E293B;
}
QProgressBar {
    background-color: #E2E8F0;
    border-radius: 4px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: #3B82F6;
    border-radius: 4px;
}
"""

ESTILO_COMPONENTES = """
/* Cards de Indicadores do Dashboard */
QFrame#CardIndicador {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
}

/* Cards das Listagens (Pacientes, Médicos, Consultas) */
QFrame#CardDado {
    background-color: #FFFFFF;
    border: 1px solid #E2E8F0;
    border-radius: 12px;
}
QFrame#CardDado:hover {
    border: 1px solid #CBD5E1;
}

/* Botões Principais (Preto/Dark igual ao Figma) */
QPushButton#BtnAcaoPrincipal {
    background-color: #0F172A;
    color: #FFFFFF;
    font-size: 13px;
    font-weight: bold;
    border-radius: 8px;
    padding: 8px 16px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QPushButton#BtnAcaoPrincipal:hover {
    background-color: #1E293B;
}

/* Inputs, ComboBoxes e Seletores dos Modais */
QLineEdit, QComboBox, QDateEdit, QTimeEdit {
    background-color: #FFFFFF;
    border: 1px solid #CBD5E1;
    border-radius: 8px;
    padding: 8px 12px;
    color: #334155;
    font-size: 13px;
    font-family: 'Segoe UI', Arial, sans-serif;
}
QLineEdit:focus, QComboBox:focus, QDateEdit:focus, QTimeEdit:focus {
    border: 1px solid #2563EB;
}

/* Estilização interna de Labels */
QLabel {
    font-family: 'Segoe UI', Arial, sans-serif;
}

/* Modais Pop-up */
QDialog {
    background-color: #FFFFFF;
}
"""
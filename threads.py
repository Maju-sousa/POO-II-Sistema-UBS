from PySide6.QtCore import QThread, Signal

import gerenciador

class OperacaoArquivoWorker(QThread):
    progresso = Signal(int)
    concluido = Signal(bool, str)

    def __init__(self, gerenciador, acao, *args):
        super().__init__()
        self.gerenciador = gerenciador
        self.acao = acao
        self.args = args

    def run(self):
        try:
            self.acao(*self.args)
            for p in self.gerenciador.salvar_dados():
                self.progresso.emit(p)
            self.concluido.emit(True, "Operação realizada e salva com sucesso!")
        except Exception as e:
            self.concluido.emit(False, str(e))

class CarregarDadosWorker(QThread):
    # Sinal emitido quando a leitura terminar
        dados_carregados = Signal()

        def __init__(self, gerenciador):
            super().__init__()
            self.gerenciador = gerenciador

        def run(self):
            # Esta função roda em segundo plano, sem travar a interface
            self.gerenciador.carregar_dados()
            self.dados_carregados.emit()

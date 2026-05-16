from PySide6.QtCore import QThread, Signal

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
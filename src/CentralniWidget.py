from PySide2 import QtWidgets

class CentralniWidget(QtWidgets.QWidget):
    def __init__(self, title, parent):
        super().__init__()
        self.boxLayout = QtWidgets.QVBoxLayout()
        self.textEdit1 = QtWidgets.QTextEdit(self)
        self.textEdit2 = QtWidgets.QTextEdit(self)
        self.boxLayout.addWidget(self.textEdit1)
        self.boxLayout.addWidget(self.textEdit2)
        self.setLayout(self.boxLayout)
    
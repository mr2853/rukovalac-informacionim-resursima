from PySide2 import QtWidgets

class CentralniWidget(QtWidgets.QWidget):
    def __init__(self, title, parent):
        super().__init__()
        self.box_layout = QtWidgets.QVBoxLayout()
        self.text_edit1 = QtWidgets.QTextEdit(self)
        self.text_edit2 = QtWidgets.QTextEdit(self)
        self.box_layout.addWidget(self.text_edit1)
        self.box_layout.addWidget(self.text_edit2)
        self.set_layout(self.box_layout)
    
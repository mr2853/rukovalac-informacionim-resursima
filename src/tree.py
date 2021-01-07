from PySide2.QtWidgets import QGridLayout, QPushButton, QTreeView


class Tree(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.zatvori = QPushButton("Zatvaranje")
        self.layout = QGridLayout()
        # self.layout.addWidget(self.zatvori)
        self.setLayout(self.layout)
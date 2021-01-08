from PySide2 import QtCore
from PySide2.QtWidgets import QGridLayout, QPushButton, QTreeView, QVBoxLayout


class Tree(QTreeView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_layout = QVBoxLayout()
        self.sub_layout = QVBoxLayout()
        self.main_layout.addLayout(self.sub_layout)
        self.setLayout(self.main_layout)
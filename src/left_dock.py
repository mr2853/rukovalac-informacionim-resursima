from PySide2 import QtWidgets, QtCore
from PySide2 import QtWidgets
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QStyleOptionViewItem

class LeftDock(QtWidgets.QDockWidget):
    kliknut = QtCore.Signal(str)
    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath("src\\podaci\\metaPodaci\\")

        self.tree = QtWidgets.QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index("src\\podaci\\metaPodaci\\"))
        self.tree.clicked.connect(self.file_clicked)
        self.setWidget(self.tree)

    def file_clicked(self, index):
        path = self.model.filePath(index)
        self.kliknut.emit(path)
    
    # def change(self):
    #     paint = QPainter()
    #     style = QStyleOptionViewItem()
    #     style.WrapText = "neki tekst"
    #     index = QtCore.QModelIndex()
    #     index.child(0,0)
    #     self.tree.drawRow(paint, style, index)
    #     paint.drawText = "da"
    
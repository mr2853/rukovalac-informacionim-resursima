from PySide2 import QtWidgets, QtCore
from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QComboBox, QStyleOptionViewItem, QVBoxLayout
from klase.file_system import FileSystem
from tree import Tree

class LeftDock(QtWidgets.QDockWidget):
    kliknut = QtCore.Signal(str)
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.main_layout = QVBoxLayout()
        self.model = FileSystem(self)
        self.model.setRootPath("podaci\\podaci")

        self.setFeatures(self.DockWidgetFeature.NoDockWidgetFeatures)
        self.tree = Tree()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index("podaci\\podaci")) 
        self.tree.hideColumn(1) 
        self.tree.hideColumn(2)
        self.tree.hideColumn(3)
        # self.tree.setColumnWidth(0,250)
        self.tree.setRowHidden(0, self.tree.rootIndex(), True) 
        self.tree.clicked.connect(self.file_clicked)
        self.main_layout.addWidget(self.tree)
        
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
    
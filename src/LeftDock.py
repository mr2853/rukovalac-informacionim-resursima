from PySide2 import QtWidgets, QtCore
from PySide2 import QtWidgets
class LeftDock(QtWidgets.QDockWidget):
    kliknut = QtCore.Signal(str)
    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath("student-service\\src\\")

        self.tree = QtWidgets.QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index("student-service\\src\\"))
        self.tree.clicked.connect(self.file_clicked)
        self.setWidget(self.tree)

    def file_clicked(self, index):
        print(self.model.filePath(index))
        path = self.model.filePath(index)
        self.kliknut.emit(path)
    
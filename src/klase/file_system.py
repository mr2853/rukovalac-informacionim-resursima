from PySide2 import QtGui, QtWidgets
from PySide2.QtCore import Qt

class FileSystem(QtWidgets.QFileSystemModel):
    def __init__(self, parent=None):
        super().__init__(parent)

    def data(self, index, role=Qt.DecorationRole):
        if role == Qt.DecorationRole:
            putanja = self.filePath(index)
            
            if putanja.find("_ser") != -1:
                return QtGui.QIcon("src/ikonice/serijska.png")
            elif putanja.find("_sek") != -1:
                return QtGui.QIcon("src/ikonice/sekvencijalna.png")
            
        return QtWidgets.QFileSystemModel.data(self, index, role)


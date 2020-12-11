from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

class ToolBar(QtWidgets.QToolBar):
    def __init__(self, main, parent=None):
        super().__init__()

        self.tool_bar = QtWidgets.QToolBar(parent=None)
        self.tool_bar.setIconSize(QtCore.QSize(30,30))
        self.tool_bar.setFixedHeight(45)
        
        self.create = QtWidgets.QAction(QtGui.QIcon("ikonice/create.png"),'Kreiraj datoteku',main)
        self.create_o = QtWidgets.QAction(QtGui.QIcon("ikonice/add.jpg"),"Dodaj u datoteku", main)
        self.change = QtWidgets.QAction(QtGui.QIcon("ikonice/change.png"),"Izmeni", main)
        self.remove = QtWidgets.QAction(QtGui.QIcon("ikonice/delete.png"),"Izbrisi", main)
        self.rename = QtWidgets.QAction(QtGui.QIcon("ikonice/rename.png"),"Preimenuj", main)
        self.tool_bar.addAction(self.create)
        self.tool_bar.addAction(self.create_o)
        self.tool_bar.addAction(self.change)
        self.tool_bar.addAction(self.remove)
        self.tool_bar.addAction(self.rename)
        self.setIconSize(QtCore.QSize(30,30))
        main.addToolBar(self.tool_bar)
        

        



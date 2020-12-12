from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

class ToolBar(QtWidgets.QToolBar):
    def __init__(self, main, parent=None):
        super().__init__()

        self.tool_bar = QtWidgets.QToolBar(parent=None)
        self.tool_bar.setIconSize(QtCore.QSize(30,30))
        self.tool_bar.setFixedHeight(45)
        
        self.kreiraj_datoteku = QtWidgets.QAction(QtGui.QIcon("src/ikonice/kreiraj.png"),'Kreiraj datoteku',main)
        self.dodaj = QtWidgets.QAction(QtGui.QIcon("src/ikonice/dodaj.png"),"Dodaj u datoteku", main)
        self.izmeni = QtWidgets.QAction(QtGui.QIcon("src/ikonice/promjeni.png"),"Izmeni datoteku", main)
        self.izmeni_tabelu = QtWidgets.QAction(QtGui.QIcon("src/ikonice/izmeni_tabelu.png"),"Izmeni tabelu", main)
        self.ukloni = QtWidgets.QAction(QtGui.QIcon("src/ikonice/izbrisi.png"),"Izbrisi datoteku", main)
        self.ukloni_tabela = QtWidgets.QAction(QtGui.QIcon("src/ikonice/izbrisi_tabela.png"),"Ukloni iz tabele", main)
        self.preimenuj = QtWidgets.QAction(QtGui.QIcon("src/ikonice/preimenuj.png"),"Preimenuj datoteku", main)
        self.pretrazi = QtWidgets.QAction(QtGui.QIcon("src/ikonice/pretraga.png"),"Pretrazi tabelu", main)
        self.tool_bar.addAction(self.kreiraj_datoteku)
        self.tool_bar.addAction(self.dodaj)
        self.tool_bar.addAction(self.izmeni)
        self.tool_bar.addAction(self.ukloni)
        self.tool_bar.addAction(self.preimenuj)
        self.tool_bar.addAction(self.izmeni_tabelu)
        self.tool_bar.addAction(self.ukloni_tabela)
        
        self.tool_bar.addAction(self.pretrazi)
        self.setIconSize(QtCore.QSize(30,30))
        main.addToolBar(self.tool_bar)
        

        



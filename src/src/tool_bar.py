from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

class ToolBar(QtWidgets.QToolBar):
    def __init__(self, main, parent=None):
        super().__init__()

        self.tool_bar = QtWidgets.QToolBar(parent=None)
        self.tool_bar.setIconSize(QtCore.QSize(30,30))
        self.tool_bar.setFixedHeight(45)
        
        # self.kreiraj_datoteku = QtWidgets.QAction(QtGui.QIcon("src/ikonice/kreiraj.png"),'Kreiraj datoteku',main)
        self.dodaj = QtWidgets.QAction(QtGui.QIcon("src/ikonice/dodaj.png"),"Dodaj u tabelu", main)
        self.izmeni_tabelu = QtWidgets.QAction(QtGui.QIcon("src/ikonice/izmeni_tabelu.png"),"Izmeni u tabeli", main)
        self.ukloni_iz_tabele = QtWidgets.QAction(QtGui.QIcon("src/ikonice/izbrisi_tabela.png"),"Ukloni iz tabele", main)
        self.pretrazi = QtWidgets.QAction(QtGui.QIcon("src/ikonice/pretraga.png"),"Pretrazi tabelu", main)
        self.spoji_datoteke = QtWidgets.QAction(QtGui.QIcon("src/ikonice/spoji.png"),"Spoji datoteke", main)
        # self.izmeni = QtWidgets.QAction(QtGui.QIcon("src/ikonice/promjeni.png"),"Izmeni datoteku", main)
        # self.ukloni = QtWidgets.QAction(QtGui.QIcon("src/ikonice/izbrisi.png"),"Izbrisi datoteku", main)
        # self.preimenuj = QtWidgets.QAction(QtGui.QIcon("src/ikonice/preimenuj.png"),"Preimenuj datoteku", main)
        # self.podeli_datoteku = QtWidgets.QAction(QtGui.QIcon("src/ikonice/podeli.png"),"Podeli datoteku", main)

        # self.tool_bar.addAction(self.kreiraj_datoteku)
        self.tool_bar.addAction(self.dodaj)
        # self.tool_bar.addAction(self.izmeni)
        # self.tool_bar.addAction(self.ukloni)
        # self.tool_bar.addAction(self.preimenuj)
        self.tool_bar.addAction(self.izmeni_tabelu)
        self.tool_bar.addAction(self.ukloni_iz_tabele)
        self.tool_bar.addAction(self.pretrazi)
        self.tool_bar.addAction(self.spoji_datoteke)
        # self.tool_bar.addAction(self.podeli_datoteku)
        
        self.setIconSize(QtCore.QSize(30,30))
        main.addToolBar(self.tool_bar)
        

        


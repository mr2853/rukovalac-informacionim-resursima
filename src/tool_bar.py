from PySide2 import QtWidgets
from PySide2 import QtGui
from PySide2 import QtCore

class ToolBar(QtWidgets.QToolBar):
    def __init__(self, main, parent=None):
        super().__init__()

        self.tool_bar = QtWidgets.QToolBar(parent=None)
        self.tool_bar.setIconSize(QtCore.QSize(30,30))
        self.tool_bar.setFixedHeight(45)
        
        # self.kreiraj_datoteku = QtWidgets.QAction(QtGui.QIcon("src/ikonice/kreiraj.png"),'Kreiranje datoteku',main)
        self.dodaj = QtWidgets.QAction(QtGui.QIcon("src/ikonice/dodaj.png"),"Dodavanje u tabelu", main)
        self.izmeni_tabelu = QtWidgets.QAction(QtGui.QIcon("src/ikonice/izmeni_tabelu.png"),"Izmena u tabeli", main)
        self.ukloni_iz_tabele = QtWidgets.QAction(QtGui.QIcon("src/ikonice/izbrisi_tabela.png"),"Uklanjanje iz tabele", main)
        self.pretrazi = QtWidgets.QAction(QtGui.QIcon("src/ikonice/pretraga.png"),"Pretrazivanje tabele", main)
        self.ponisti_pretragu = QtWidgets.QAction(QtGui.QIcon("src/ikonice/ponisti_pretragu.png"),"Ponistavanje pretrage", main)
        self.spoji_datoteke = QtWidgets.QAction(QtGui.QIcon("src/ikonice/spoji.png"),"Spajanje datoteka", main)
        # self.izmeni = QtWidgets.QAction(QtGui.QIcon("src/ikonice/promjeni.png"),"Izmena datoteke", main)
        # self.ukloni = QtWidgets.QAction(QtGui.QIcon("src/ikonice/izbrisi.png"),"Brisanje datoteke", main)
        # self.preimenuj = QtWidgets.QAction(QtGui.QIcon("src/ikonice/preimenuj.png"),"Preimenovanje datoteke", main)
        # self.podeli_datoteku = QtWidgets.QAction(QtGui.QIcon("src/ikonice/podeli.png"),"Podela datoteke", main)

        # self.tool_bar.addAction(self.kreiraj_datoteku)
        self.tool_bar.addAction(self.dodaj)
        # self.tool_bar.addAction(self.izmeni)
        # self.tool_bar.addAction(self.ukloni)
        # self.tool_bar.addAction(self.preimenuj)
        self.tool_bar.addAction(self.izmeni_tabelu)
        self.tool_bar.addAction(self.ukloni_iz_tabele)
        self.tool_bar.addAction(self.pretrazi)
        self.tool_bar.addAction(self.ponisti_pretragu)
        self.tool_bar.addAction(self.spoji_datoteke)
        # self.tool_bar.addAction(self.podeli_datoteku)
        
        self.setIconSize(QtCore.QSize(30,30))
        main.addToolBar(self.tool_bar)
        

        



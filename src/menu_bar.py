from PySide2 import QtWidgets
from PySide2 import QtGui

class MenuBar(QtWidgets.QMenuBar):
    def __init__(self, main, parent):
        super().__init__(parent)


        self.menu_bar = QtWidgets.QMenuBar(parent=None)
        self.datoteka=self.menu_bar.addMenu("Datoteka")
        self.pomoc = self.menu_bar.addMenu("Pomoc")

        self.datoteka_akcija = QtWidgets.QAction(QtGui.QIcon("src/ikonice/opis.png"),"O softverskom proizvodu",self.menu_bar)
        self.datoteka.addAction(self.datoteka_akcija)
        self.pomoc_akcija = QtWidgets.QAction(QtGui.QIcon("src/ikonice/upustvo.png"),"Tehnicka podrska",self.menu_bar)
        self.pomoc.addAction(self.pomoc_akcija)


        self.datoteka_akcija.triggered.connect(self.o_aplikaciji)
        self.pomoc_akcija.triggered.connect(self.tehnicka_pomoc)
        
        
        main.setMenuBar(self.menu_bar)
     
    

    def o_aplikaciji(self):
        poruka = QtWidgets.QMessageBox()
        icon = QtGui.QIcon("src/ikonice/logo.jpg")
        poruka.setWindowIcon(icon)
        poruka.setWindowTitle("O aplikaciji")
        poruka.setText("Pred Vama je GUI orjentisani, interaktivni, dogadjajima upravljani softverski alat za upravljanje informacionim resursima.")
        
            
        poruka.exec_()

    def tehnicka_pomoc(self):
        poruka = QtWidgets.QMessageBox()
        icon = QtGui.QIcon("src/ikonice/logo.jpg")
        poruka.setWindowIcon(icon)
        poruka.setWindowTitle("Tehnicka pomoc")
        poruka.setText("Ukoliko Vam je potrebna pomoc, molimo Vas posaljite e-mail na: tehnickapodrska@singimail.rs")
        
            
        poruka.exec_()



        
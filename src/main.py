import sys
from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox
from prijava import Prijava
from pocetna_strana import PocetnaStrana

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # klasa = global()[tabela.izMetaPodataka["klasa"]](dobavi selektovanog)
    # sakrije tabelu
    # layout
    # for i in range(....):
    #     self.nazivi_atributa[i] = noviInput()
    #     layout.add(self.nazivi_atributa[i])
    
    # dodaj
    # izmeni
    
    
    # form = Prijava()
    # form.show()
    # with open("style.qss", "r") as f:
    #     _style = f.read()
    #     app.setStyleSheet(_style)

    pocetna_strana = PocetnaStrana()
    
    sys.exit(app.exec_())
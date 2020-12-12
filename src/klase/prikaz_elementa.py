from .genericka_klasa import GenerickaKlasa
from PySide2 import QtWidgets

class PrikazElementa(QtWidgets.QWidget):
    def __init__(self, parent, lista_atributa, lista_podataka=[]):
        super().__init__()
        # parent.table.hide()
        # parent.tab_widget.hide()
        self.lista_atr = []
        self.lista_kriterijuma = []
        if len(lista_podataka) != 0:
            self.element = GenerickaKlasa(lista_atributa, lista_podataka)
        else:
            self.element = GenerickaKlasa([],[])

        for i in range(len(lista_atributa)):
            # ime = "input"
            # ime += str(i+1)
            naziv = lista_atributa[i][0].upper()

            for s in range(1, len(lista_atributa[i])):
                if lista_atributa[i][s] == "_":
                    naziv += " "
                elif lista_atributa[i][s].isupper():
                    naziv += lista_atributa[i][s].upper()
                else:
                    naziv += lista_atributa[i][s]

            text, ok = QtWidgets.QInputDialog.getText(self, 'Unos podataka:', naziv+":", QtWidgets.QLineEdit.Normal)
            
            if ok and len(text.strip()) != 0:
                self.element.__setattr__(lista_atributa[i], str(text))
                self.lista_atr.append(lista_atributa[i])
                self.lista_kriterijuma.append(text)

        
        

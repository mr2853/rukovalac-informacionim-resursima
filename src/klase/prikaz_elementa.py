from .genericka_klasa import GenerickaKlasa
from PySide2 import QtWidgets

class PrikazElementa(QtWidgets.QWidget):
    def __init__(self, parent, lista_atributa, element=None):
        super().__init__(parent)
        # parent.table.hide()
        # parent.tab_widget.hide()
        self.lista_atr = [] # ovu listu koristim za pretragu, dodaju se samo
        # atributi cija input polja nisu prazna, i onda znam po kojim atributima
        # da vrsim pretragu
        self.lista_kriterijuma = [] # lista kriterijuma, isto kao lista gore sto
        # cuva nazive atributa, ova lista cuva vrednosti tih atributa
        if element != None:
            self.element = element
        else:
            self.element = GenerickaKlasa([],[])

        for i in range(len(lista_atributa)):
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

        
        

from .genericka_klasa import GenerickaKlasa
from PySide2 import QtWidgets

class PrikazElementa(QtWidgets.QWidget):
    def __init__(self, parent, meta_podaci, tip, element=None): # tip == 0 -dodavanje / tip == 1 -pretraga
        super().__init__(parent)
        lista_atributa = meta_podaci[5].split(",")
        lista_tipovi_atributa = meta_podaci[6].split(",")
        lista_duzine_atributa = meta_podaci[7].split(",")
        lista_obaveznosti_atributa = meta_podaci[8].split(",")
        lista_lista_kljuceva = meta_podaci[12].split(",")
        # parent.table.hide()
        # parent.tab_widget.hide()
        self.lista_atr = [] # ovu listu koristim za pretragu, dodaju se samo
        # atributi cija input polja nisu prazna, i onda znam po kojim atributima
        # da vrsim pretragu
        self.lista_kriterijuma = [] # lista kriterijuma, isto kao lista gore sto
        # cuva nazive atributa, ova lista cuva vrednosti tih atributa
        self.izmena = False
        if element != None:
            self.element = element
            self.izmena = True
        else:
            self.element = GenerickaKlasa([],[])

        for i in range(len(lista_atributa)):
            naziv = lista_atributa[i][0].upper()

            for s in range(1, len(lista_atributa[i])):
                if lista_atributa[i][s] == "_":
                    naziv += " "
                else:
                    naziv += lista_atributa[i][s]

            text, ok = QtWidgets.QInputDialog.getText(self, 'Unos podataka:', naziv+":", QtWidgets.QLineEdit.Normal)
            
            if ok and len(text.strip()) != 0:
                self.element.__setattr__(lista_atributa[i], str(text))
                self.lista_atr.append(lista_atributa[i])
                self.lista_kriterijuma.append(text)

        
        

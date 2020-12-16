from .genericka_klasa import GenerickaKlasa
from PySide2 import QtWidgets, QtGui
import csv

class PrikazElementa(QtWidgets.QDialog):
    def __init__(self, parent, meta_podaci, element=None): # tip == 0 -dodavanje / tip == 1 -pretraga
        super(PrikazElementa,self).__init__(parent)
        self.lista_atributa = meta_podaci[5].split(",")
        self.lista_tipovi_atributa = meta_podaci[6].split(",")
        self.lista_duzine_atributa = meta_podaci[7].split(",")
        self.lista_obaveznosti_atributa = meta_podaci[8].split(",")
        self.lista_lista_kljuceva = meta_podaci[12].split(",")
        self.tip_datoteke = meta_podaci[1]
        self.relativna_putanja = meta_podaci[2]
        self.sufiks = meta_podaci[3]
        self.podaci = meta_podaci[4]
        self.novi_objekat = []
       
        self.setWindowTitle("Dodavanje")
        icon = QtGui.QIcon("src/ikonice/logo.jpg")
        self.setWindowIcon(icon)
        self.layout = QtWidgets.QGridLayout()
        self.dugme = QtWidgets.QPushButton("Dodaj")
        #self.dugme = QtWidgets.QPushButton("Dodaj")
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

        for i in range(len(self.lista_atributa)):
            naziv = self.lista_atributa[i][0].upper()

            for s in range(1, len(self.lista_atributa[i])):
                if self.lista_atributa[i][s] == "_":
                    naziv += " "
                else:
                    naziv += self.lista_atributa[i][s]
            ime = QtWidgets.QLabel(naziv + " :")
            self.layout.addWidget(ime)
            #if self.li
            self.__setattr__(self.lista_atributa[i], QtWidgets.QLineEdit())

            
            
            
            self.__getattribute__(self.lista_atributa[i]).setPlaceholderText("Do " + self.lista_duzine_atributa[i] + " karaktera")
            self.layout.addWidget(self.__getattribute__(self.lista_atributa[i]))
           
            
        
        self.layout.addWidget(self.dugme)
        self.setLayout(self.layout)
        self.dugme.clicked.connect(self.dugme_kliknuto)
        
        
        
        self.show()

    def dugme_kliknuto(self):
        try:
            for i in range(len(self.lista_atributa)):
                vrijednost = self.__getattribute__(self.lista_atributa[i]).text()

                if len(vrijednost) <= int(self.lista_duzine_atributa[i]):
                    if bool(self.lista_obaveznosti_atributa[i]) == True:
                        if vrijednost == "":
                            poruka = QtWidgets.QMessageBox()
                            poruka.setText("Ovo polje ne sme biti prazno! Pokusajte ponovo!")
                            poruka.exec_()
                            self.close()
                            return

                    if self.lista_tipovi_atributa[i] == "int":
                        if isinstance(int(vrijednost),int) == False:
                            poruka = QtWidgets.QMessageBox()
                            poruka.setText("Pogresna vrednost! Pokusajte ponovo!")
                            poruka.exec_()
                            self.close()
                            return

                    if self.lista_tipovi_atributa[i] == "float":
                        if isinstance(float(vrijednost),float) == False:
                            poruka = QtWidgets.QMessageBox()
                            poruka.setText("Pogresna vrednost! Pokusajte ponovo!")
                            poruka.exec_()
                            self.close()
                            return

                    self.novi_objekat.append(vrijednost)
                    self.close()
                else:
                    poruka = QtWidgets.QMessageBox()
                    poruka.setText("Prekoracili ste duzinu karaktera!")
                    poruka.exec_()
                    self.close()
                    return

            if self.novi_objekat != [] and len(self.novi_objekat) == len(self.lista_atributa):
               
                
                if self.tip_datoteke == "serijska":
                    
                    with open(self.podaci, 'a', newline='', encoding="utf-8") as f: 
                        writer = csv.writer(f, delimiter=",")
                        writer.writerow(self.novi_objekat)
                        return
                #elif self.tip_datoteke == "sekvencijalna":
                #ovdje dodati upis u sekvencijalnu datoteku
 
        except ValueError:
            print("Pogresna vrednost!")
            return    
            
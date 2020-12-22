from klase.metode import dodaj_u_serijsku, sastavi_sekvencijalnu
from .genericka_klasa import GenerickaKlasa
from PySide2.QtCore import QModelIndex
from PySide2 import QtWidgets, QtGui
from pydoc import locate
import csv
import os

class PrikazElementa(QtWidgets.QDialog): # izmena, dodaj, pretrazi
    def __init__(self, parent, meta_podaci, pretraga=False, element=None):
        super(PrikazElementa,self).__init__(parent)
        self.lista_atributa = meta_podaci[5].split(",")
        self.lista_tipovi_atributa = meta_podaci[6].split(",")
        self.lista_duzine_atributa = meta_podaci[7].split(",")
        self.lista_obaveznosti_atributa = meta_podaci[8].split(",")
        self.lista_kljuceva = meta_podaci[12].split(",")
        self.tip_datoteke = meta_podaci[1]
        self.relativna_putanja = meta_podaci[2]
        self.sufiks = meta_podaci[3]
        self.putanja_podaci = meta_podaci[4]
        self.lista = []
        self.pretraga = pretraga
        self.privremena_datoteka = "podaci/podaci/privremena_ser.csv"
        icon = QtGui.QIcon("src/ikonice/logo.jpg")
        self.setWindowIcon(icon)
        self.layout = QtWidgets.QGridLayout()
        self.tip = 0  # tip == 0 -dodavanje / tip == 1 -izmena / tip == 3 -pretraga
        
        if element != None:
            self.dugme = QtWidgets.QPushButton("Izmena")
            self.setWindowTitle("Izmena")
            self.tip = 1
        elif element == None and not pretraga:
            self.dugme = QtWidgets.QPushButton("Dodaj")
            self.setWindowTitle("Dodavanje")
            self.tip = 0
        else:
            self.dugme = QtWidgets.QPushButton("Pretraga")
            self.setWindowTitle("Pretraga")
            self.tip = 2
            
        self.zatvori = QtWidgets.QPushButton("Zatvori")
        #self.dugme = QtWidgets.QPushButton("Dodaj")
        # parent.table.hide()
        # parent.tab_widget.hide()
        self.lista_atr = [] # ovu listu koristim za pretragu, dodaju se samo
        # atributi cija input polja nisu prazna, i onda znam po kojim atributima
        # da vrsim pretragu
        self.lista_kriterijuma = [] # lista kriterijuma, isto kao lista gore sto
        # cuva nazive atributa, ova lista cuva vrednosti tih atributa

        for i in range(len(self.lista_atributa)):
            naziv = self.lista_atributa[i][0].upper()

            for s in range(1, len(self.lista_atributa[i])):
                if self.lista_atributa[i][s] == "_":
                    naziv += " "
                else:
                    naziv += self.lista_atributa[i][s]
            ime = QtWidgets.QLabel(naziv + " :")
            self.layout.addWidget(ime)
            self.__setattr__(self.lista_atributa[i], QtWidgets.QLineEdit())
            if element == None and not pretraga:
                self.__getattribute__(self.lista_atributa[i]).setPlaceholderText("Do " + self.lista_duzine_atributa[i] + " karaktera")
            elif element != None:
                self.element = element
                self.__getattribute__(self.lista_atributa[i]).setText(element.__getattribute__(self.lista_atributa[i]))
            self.layout.addWidget(self.__getattribute__(self.lista_atributa[i]))
            
        self.layout.addWidget(self.dugme)
        self.layout.addWidget(self.zatvori)
        self.setLayout(self.layout)
        self.dugme.clicked.connect(self.dugme_kliknuto)
        self.zatvori.clicked.connect(self.zatvori_prikaz)
        
        if self.tip == 1:
            self.original_elem = GenerickaKlasa([],[])
            self.element = element
            for i in range(len(self.lista_kljuceva)):
                self.original_elem.__setattr__(self.lista_kljuceva[i], self.element.__getattribute__(self.lista_kljuceva[i]))
        else:
            self.element = GenerickaKlasa([],[])
        
        
        self.show()
    
    def sacuvaj_podatke(self):
        if os.path.exists(self.privremena_datoteka):
            if self.tip_datoteke == "sekvencijalna":
                if sastavi_sekvencijalnu(self):
                    if os.path.exists(self.privremena_datoteka):
                        os.remove(self.privremena_datoteka)
                    else:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText("Privremena datoteka ne postoji")
                        msgBox.exec_()

    def zatvori_prikaz(self):
        self.close()

    def closeEvent(self, event):
        self.sacuvaj_podatke()
        event.accept()

    def dugme_kliknuto(self):
        try:
            for i in range(len(self.lista_atributa)):
                vrijednost = self.__getattribute__(self.lista_atributa[i]).text()

                if len(vrijednost) <= int(self.lista_duzine_atributa[i]):
                    if bool(self.lista_obaveznosti_atributa[i]) == True and not self.pretraga:
                        if vrijednost == "":
                            poruka = QtWidgets.QMessageBox()
                            poruka.setText(self.lista_atributa[i]+" polje ne sme biti prazno! Pokusajte ponovo!")
                            poruka.exec_()
                            return
                    
                    try:
                        if isinstance(locate(self.lista_tipovi_atributa[i])(vrijednost), locate(self.lista_tipovi_atributa[i])) == False:
                            poruka = QtWidgets.QMessageBox()
                            poruka.setText(self.lista_atributa[i]+" polje pogresna vrednost! Pokusajte ponovo!")
                            poruka.exec_()
                            return
                    except ValueError:
                        msgBox = QtWidgets.QMessageBox()
                        msgBox.setText(self.lista_atributa[i]+" polje pogresna vrednost! Pokusajte ponovo!")
                        msgBox.exec_()
                        return

                    self.element.__setattr__(self.lista_atributa[i], vrijednost)
                else:
                    poruka = QtWidgets.QMessageBox()
                    poruka.setText("Prekoracili ste duzinu karaktera!")
                    poruka.exec_()
                    return

                #self.__getattribute__(self.lista_atributa[i]).setPlaceholderText("Do " + self.lista_duzine_atributa[i] + " karaktera")
                
            
            if self.tip == 1:
                self.parent().table.model().lista_prikaz = []

                with open(self.putanja_podaci, 'r',newline='') as csvfile:
                    spamreader = csv.reader(csvfile, delimiter = "\n")
                    counter = 0
                    prva_linija = True
                    for row in spamreader:
                        if prva_linija:
                            prva_linija = False
                            continue
                        if row[0] == "":
                            break
            
                        objekat = GenerickaKlasa(self.lista_atributa, row[0].split(","))
                        nadjen = True
                        
                        for i in range(len(self.lista_kljuceva)):
                            if objekat.__getattribute__(self.lista_kljuceva[i]) !=  self.original_elem.__getattribute__(self.lista_kljuceva[i]):
                                nadjen = False
                        if not nadjen:
                            self.parent().table.model().lista_prikaz.append(objekat)
                        else:
                            for i in range(len(self.lista_atributa)):
                                objekat.__setattr__(self.lista_atributa[i], self.element.__getattribute__(self.lista_atributa[i]))

                            self.parent().table.model().lista_prikaz.append(objekat)
                            
                        counter += 1
    
                with open(self.putanja_podaci, 'w', newline='') as f:
                    writer = csv.writer(f, delimiter = ",")
                    writer.writerow([self.parent().putanja_meta])
                    for i in range(len(self.parent().table.model().lista_prikaz)):
                        tekst = ""
                        for j in range(len(self.lista_atributa)):
                            tekst += str(self.parent().table.model().lista_prikaz[i].__getattribute__(self.lista_atributa[j]))
                            if j < len(self.lista_atributa)-1:
                                tekst += ","
                                
                        novi_red = tekst.split(",")
                        writer.writerow(novi_red)

                    top = QModelIndex()
                    top.child(0,0)
                    bottom = QModelIndex()
                    bottom.child(len(self.parent().table.model().lista_prikaz), self.parent().table.model().broj_kolona)
                    self.parent().table.dataChanged(top, bottom) # da refresuje tabelu od top indexa to bottom indexa

            elif self.tip == 0:
                if self.tip_datoteke == "serijska":
                    dodaj_u_serijsku(self.element, self.lista_atributa, self.putanja_podaci, self.parent().putanja)
                    self.parent().table.model().beginInsertRows(QModelIndex(), 0, 0)
                    model = self.parent().table.model()
                    model.lista_prikaz.append(self.element)
                    self.parent().table.setModel(model)
                    self.parent().table.model().endInsertRows()

                elif self.tip_datoteke == "sekvencijalna":
                    dodaj_u_serijsku(self.element, self.lista_atributa, self.privremena_datoteka, self.parent().putanja)
                
                top = QModelIndex()
                top.child(0,0)
                bottom = QModelIndex()
                bottom.child(len(self.parent().table.model().lista_prikaz), self.parent().table.model().broj_kolona)
                self.parent().table.dataChanged(top, bottom) # da refresuje tabelu od top indexa to bottom indexa
                
            elif self.tip == 2:
                print("pretraga, bice odradjeno")
            
        except ValueError:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Pogresna vrednost")
            msgBox.exec_()
            return    
            
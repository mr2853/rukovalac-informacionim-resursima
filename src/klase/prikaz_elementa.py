from configparser import Error
from klase.metode import dodaj_u_serijsku, sastavi_sekvencijalnu
from .genericka_klasa import GenerickaKlasa
from PySide2.QtCore import QModelIndex
from PySide2 import QtWidgets, QtGui, QtCore
from pydoc import locate
import csv
import mysql
import os

class PrikazElementa(QtWidgets.QDialog): # izmena, dodaj, pretrazi
    def __init__(self, parent, pretraga=False, element=None):
        super(PrikazElementa,self).__init__(parent)
        meta_podaci = parent.meta_podaci  #kada kliknemo saljemo meta podatke u prikaz
        self.lista_atributa = meta_podaci[5].split(",")
        self.lista_naziva_atributa = meta_podaci[5].split(",")
        self.lista_tipovi_atributa = meta_podaci[6].split(",")
        self.lista_duzine_atributa = meta_podaci[7].split(",")
        self.lista_obaveznosti_atributa = meta_podaci[8].split(",")
        self.lista_kljuceva = meta_podaci[11].split(",")
        self.tip_datoteke = meta_podaci[1]
        self.relativna_putanja = meta_podaci[2]
        self.sufiks = meta_podaci[3]
        self.putanja_podaci = meta_podaci[4]
        self.lista = []
        self.primarni_kljucevi=[]
        if self.tip_datoteke == "sekvencijalna":
            self.roditelji = meta_podaci[12].split(",")
            self.broj_kljuceva = meta_podaci[13].split(",")
            self.pozicije_u_formi = meta_podaci[14].split(",")
            self.pozicije_u_datoteci = meta_podaci[15].split(",")
            
        
        self.putanja_kljucevi ="podaci/podaci/sekvencijalne/"
        self.pretraga = pretraga
        self.privremena_datoteka = "podaci/podaci/privremena_ser.csv"
        icon = QtGui.QIcon("src/ikonice/logo.jpg")
        self.setWindowIcon(icon)
        self.layout = QtWidgets.QGridLayout()
        
        
        
        
        self.setWindowFlags(self.windowFlags()
                ^ QtCore.Qt.WindowContextHelpButtonHint)
        self.tip = 0  # tip == 0 -dodavanje / tip == 1 -izmena / tip == 2 -pretraga
        
        if element != None:
            self.dugme = QtWidgets.QPushButton("Izmena")
            self.setWindowTitle("Izmena")
            self.tip = 1
        elif element == None and not pretraga:
            self.dugme = QtWidgets.QPushButton("Dodavanje")
            self.setWindowTitle("Dodavanje")
            self.tip = 0
        else:
            self.dugme = QtWidgets.QPushButton("Pretraga")
            self.setWindowTitle("Pretraga")
            self.tip = 2
            
        self.zatvori = QtWidgets.QPushButton("Zatvaranje")
        self.lista_atr = [] # ovu listu koristim za pretragu, dodaju se samo
        # atributi cija input polja nisu prazna, i onda znam po kojim atributima
        # da vrsim pretragu
        self.lista_kriterijuma = [] # lista kriterijuma, isto kao lista gore sto
        # cuva nazive atributa, ova lista cuva vrednosti tih atributa
        self.lista_vece_manje = []
        m=0
        self.blocked = False
        for i in range(len(self.lista_atributa)):
            naziv = self.lista_atributa[i][0].upper()

            for s in range(1, len(self.lista_atributa[i])):
                if self.lista_atributa[i][s] == "_":
                    naziv += " "
                else:
                    naziv += self.lista_atributa[i][s]
            
            ime = QtWidgets.QLabel(naziv + " :")
            self.layout.addWidget(ime,m,0)
            self.__setattr__(self.lista_atributa[i], QtWidgets.QLineEdit())

            if self.tip == 2:
                self.__setattr__(self.lista_atributa[i]+"_vece_manje", QtWidgets.QComboBox())
                self.__getattribute__(self.lista_atributa[i]+"_vece_manje").addItem("jednako")
                if self.lista_tipovi_atributa[i] !=  "str":
                    self.__getattribute__(self.lista_atributa[i]+"_vece_manje").addItem("manje od")
                    self.__getattribute__(self.lista_atributa[i]+"_vece_manje").addItem("manje ili jednako od")
                    self.__getattribute__(self.lista_atributa[i]+"_vece_manje").addItem("vece od")
                    self.__getattribute__(self.lista_atributa[i]+"_vece_manje").addItem("vece ili jednako od")

                self.__getattribute__(self.lista_atributa[i]+"_vece_manje").setCurrentIndex(0)
                self.__getattribute__(self.lista_atributa[i]+"_vece_manje").setEditable(False)

            if element == None and not pretraga:
                self.__getattribute__(self.lista_atributa[i]).setPlaceholderText("Do " + self.lista_duzine_atributa[i] + " karaktera")
                self.__getattribute__(self.lista_atributa[i]).setMaxLength(int(self.lista_duzine_atributa[i]))
                if "datum" in self.lista_naziva_atributa[i].lower():
                    self.__getattribute__(self.lista_atributa[i]).setPlaceholderText("YYYY-MM-DD")
                    
            elif element != None:
                self.element = element
                
                self.__getattribute__(self.lista_atributa[i]).setText(element.__getattribute__(self.lista_atributa[i]))
                self.__getattribute__(self.lista_atributa[i]).setMaxLength(int(self.lista_duzine_atributa[i]))
                print(self.lista_naziva_atributa[i])
              
                veze = self.parent().meta_podaci[9].split(",")
                for j in range(len(veze)):
                    if hasattr(self.parent(), "sub_table"+str(j+1)):
                        if len(self.parent().__getattribute__("sub_table"+str(j+1)).model.lista_prikaz) != 0:
                            for k in range(len(self.lista_kljuceva)):
                                if k <= i:
                                    if self.__getattribute__(self.lista_kljuceva[k]).isEnabled():
                                        self.__getattribute__(self.lista_kljuceva[k]).setDisabled(True)
                            self.blocked = True
            
            self.__getattribute__(self.lista_atributa[i]).setFixedHeight(27)
            self.layout.addWidget(self.__getattribute__(self.lista_atributa[i]),m,1)
            
            if self.tip == 2:
                self.layout.addWidget(self.__getattribute__(self.lista_atributa[i]+"_vece_manje"),m,2)
            m+=1
        self.layout.addWidget(self.dugme,m+1,0,1,3)
        self.layout.addWidget(self.zatvori,m+2,0,3,3)
        self.setLayout(self.layout)
        self.dugme.clicked.connect(self.dugme_kliknuto)
        self.zatvori.clicked.connect(self.zatvori_prikaz)
        
        if self.tip == 1:
            self.original_elem = GenerickaKlasa([],[])
            self.element = element
            for i in range(len(self.lista_atributa)):
                self.original_elem.__setattr__(self.lista_atributa[i], self.element.__getattribute__(self.lista_atributa[i]))
        else:
            self.element = GenerickaKlasa([],[])
        
        self.setMinimumWidth(500)
        self.show()
    
    
    def ucitaj_kljuceve(self,putanja, pozicija_kljuca):
        kljucevi = open(putanja,"r",encoding="utf-8")
        next(csv.reader(kljucevi,delimiter=","))
        self.primarni_kljucevi=[i.split(',')[pozicija_kljuca] for i in kljucevi.readlines()]
        return self.primarni_kljucevi
        
    def poredjenje(self, lista, vrijednost):
        brojac = 0
        for i in range(len(lista)):
            print(lista[i] +"=="+ vrijednost)
            if lista[i] == vrijednost:
                brojac +=1

        if brojac > 0:
            return True
        else:
            return False 

    def sacuvaj_podatke(self):
        if os.path.exists(self.privremena_datoteka):
            if self.tip_datoteke == "sekvencijalna":
                top = QModelIndex()
                top.child(0,0)
                self.parent().table.model().beginRemoveRows(top, 0, 0)
                if sastavi_sekvencijalnu(self):
                    if os.path.exists(self.privremena_datoteka):
                        os.remove(self.privremena_datoteka)
                    else:
                        poruka = QtWidgets.QMessageBox()
                        icon = QtGui.QIcon("src/ikonice/logo.jpg")
                        poruka.setWindowIcon(icon)
                        poruka.setWindowTitle("Upozorenje!")
                        poruka.setText("Privremena datoteka ne postoji!")
                        poruka.exec_()
                        
                self.parent().table.model().endRemoveRows()
                
                self.parent().table.model().beginInsertRows(QModelIndex(), 0, 0)
                top = QModelIndex()
                top.child(0,0)
                bottom = QModelIndex()
                bottom.child(len(self.parent().table.model().lista_prikaz), self.parent().table.model().broj_kolona)
                self.parent().table.dataChanged(top, bottom) 
                self.parent().table.model().endInsertRows()

    def zatvori_prikaz(self):
        self.close()

    def closeEvent(self, event):
        self.sacuvaj_podatke()
        event.accept()
    

    def dugme_kliknuto(self):
        try:
            for i in range(len(self.lista_atributa)):
                vrijednost = self.__getattribute__(self.lista_atributa[i]).text()
           
                if self.tip_datoteke == "sekvencijalna":
                    brojac =0
                    for o in range(len(self.broj_kljuceva)):
                        if self.broj_kljuceva != []:
                            
                            for k in range(int(self.broj_kljuceva[o])):
                                self.ucitaj_kljuceve(self.putanja_kljucevi + self.roditelji[o],int(self.pozicije_u_datoteci[brojac]))
                                vrijed = self.__getattribute__(self.lista_atributa[int(self.pozicije_u_formi[brojac])]).text()
                                brojac +=1
                              
                                if self.poredjenje(self.primarni_kljucevi,vrijed) == False:         
                                    poruka = QtWidgets.QMessageBox()
                                    icon = QtGui.QIcon("src/ikonice/logo.jpg")
                                    poruka.setWindowIcon(icon)
                                    poruka.setWindowTitle("Upozorenje!")
                                    poruka.setText(" sadrzi kljuc koji ne postoji u roditeljskoj klasi! Pokusajte ponovo!")
                                    poruka.exec_()
                                    return
                                else:
                                    continue
                                    
                                
                    

                if self.tip == 2:
                    if len(vrijednost.strip()) == 0:
                        continue

                if len(vrijednost) <= int(self.lista_duzine_atributa[i]):
                    if bool(self.lista_obaveznosti_atributa[i]) == True and self.tip != 2:
                        if vrijednost == "":
                            poruka = QtWidgets.QMessageBox()
                            icon = QtGui.QIcon("src/ikonice/logo.jpg")
                            poruka.setWindowIcon(icon)
                            poruka.setWindowTitle("Upozorenje!")
                            poruka.setText(str(self.lista_atributa[i]).capitalize()+" polje ne sme biti prazno! Pokusajte ponovo!")
                            poruka.exec_()
                            return
                    
                    try:
                        if isinstance(locate(self.lista_tipovi_atributa[i])(vrijednost), locate(self.lista_tipovi_atributa[i])) == False:
                            poruka = QtWidgets.QMessageBox()
                            icon = QtGui.QIcon("src/ikonice/logo.jpg")
                            poruka.setWindowIcon(icon)
                            poruka.setWindowTitle("Upozorenje!")
                            poruka.setText(str(self.lista_atributa[i]).capitalize()+" polje pogresna vrednost! Pokusajte ponovo!")
                            poruka.exec_()
                            return
                    except ValueError:
                        poruka = QtWidgets.QMessageBox()
                        icon = QtGui.QIcon("src/ikonice/logo.jpg")
                        poruka.setWindowIcon(icon)
                        poruka.setWindowTitle("Upozorenje!")
                        poruka.setText(str(self.lista_atributa[i]).capitalize()+" polje pogresna vrednost! Pokusajte ponovo!")
                        poruka.exec_()
                        return

                    self.element.__setattr__(self.lista_atributa[i], vrijednost)
                    self.lista_atr.append(self.lista_atributa[i])
                    self.lista_kriterijuma.append(vrijednost)
                    if self.tip == 2:
                        self.lista_vece_manje.append(self.__getattribute__(self.lista_atributa[i]+"_vece_manje").currentIndex())
                else:
                    poruka = QtWidgets.QMessageBox()
                    icon = QtGui.QIcon("src/ikonice/logo.jpg")
                    poruka.setWindowIcon(icon)
                    poruka.setWindowTitle("Upozorenje!")
                    poruka.setText(str(self.lista_atributa[i]).capitalize() + ". Prekoracili ste duzinu karaktera!")
                    poruka.exec_()
                    return
            
            if self.tip == 1:
                if not self.parent().is_baza:
                    with open(self.putanja_podaci, 'r',newline='') as csvfile:
                        spamreader = csv.reader(csvfile, delimiter = "\n")
                        counter = 0
                        prva_linija = True
                        lista = []
                        for row in spamreader:
                            if prva_linija:
                                prva_linija = False
                                continue
                            if row[0] == "":
                                break
                            
                            objekat = GenerickaKlasa(self.lista_atributa, row[0].split(","))
                            nadjen = True
                            
                            self.parent().table.model().lista_prikaz = []
                            for i in range(len(self.lista_atributa)):
                                if objekat.__getattribute__(self.lista_atributa[i]) !=  self.original_elem.__getattribute__(self.lista_atributa[i]):
                                    nadjen = False
                            if not nadjen:
                                lista.append(objekat)
                            else:
                                for i in range(len(self.lista_atributa)):
                                    objekat.__setattr__(self.lista_atributa[i], self.element.__getattribute__(self.lista_atributa[i]))

                                lista.append(objekat)
                                
                            counter += 1
                        
                        self.parent().table.model().lista_prikaz = lista

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
                else:
                    parent = self.parent().pocetna_strana
                    
                    query = "UPDATE " + self.parent().naziv + " SET "
                    block = False
                    for i in range(len(self.lista_atributa)):
                        block = False
                        if self.blocked:
                            for j in self.lista_kljuceva:
                                if self.lista_atributa[i] == j:
                                    block = True
                                    break
                        if block:
                            continue
                        query += self.lista_atributa[i] + "="
                        if self.lista_tipovi_atributa[i] == "str":
                            query += "'"
                        query += self.element.__getattribute__(self.lista_atributa[i])
                        if self.lista_tipovi_atributa[i] == "str":
                            query += "'"

                        if i < len(self.lista_atributa) - 1:
                            query += " , "
                            
                    if len(self.lista_atributa) == len(self.lista_kljuceva) and self.blocked:
                        return
                        
                    query += " WHERE "
                    for i in range(len(self.lista_kljuceva)):
                        query += self.lista_kljuceva[i] + "="
                        if self.lista_tipovi_atributa[i] == "str":
                            query += "'"

                        query += self.original_elem.__getattribute__(self.lista_kljuceva[i])
                        if self.lista_tipovi_atributa[i] == "str":
                            query += "'"

                        if i < len(self.lista_kljuceva) - 1:
                            query += " AND "
                    try:
                        parent.csor.execute(query)
                    except mysql.connector.errors.IntegrityError as e:
                        poruka = QtWidgets.QMessageBox()
                        icon = QtGui.QIcon("src/ikonice/logo.jpg")
                        poruka.setWindowIcon(icon)
                        poruka.setWindowTitle("Upozorenje!")
                        poruka.setText("Vec postoji element sa zadatim kljucem!\n"+e.msg)
                        poruka.exec_()

                    parent.connection.commit()

                    query = "SELECT * FROM " + self.parent().naziv
                    parent.csor.execute(query)
                    
                    self.parent().table.model().lista_prikaz = []
                    for result in parent.csor.fetchall():
                        lista_podataka = []
                        for i in result:
                            lista_podataka.append(str(i))
                            
                        self.parent().table.model().lista_prikaz.append(GenerickaKlasa(self.lista_atributa, lista_podataka))

                top = QModelIndex()
                top.child(0,0)
                bottom = QModelIndex()
                bottom.child(len(self.parent().table.model().lista_prikaz), self.parent().table.model().broj_kolona)
                self.parent().table.dataChanged(top, bottom) 

            elif self.tip == 0:
                if self.tip_datoteke == "sql":
                    parent = self.parent().pocetna_strana
                  
                    query = "INSERT INTO " + self.parent().naziv +" (" 
                    brojac =0
                    for i in range(len(self.lista_atributa)):
                        query += self.lista_atributa[i]
                        if brojac < len(self.lista_atributa)-1:
                            query += ", "
                        brojac += 1
                    query += ") " + "VALUES ("
                    brojac2=0
                    for i in range(len(self.lista_atributa)):
                        if self.lista_tipovi_atributa[i] == "str":
                            query += "'"+self.__getattribute__(self.lista_atributa[i]).text()+"'"
                        else:
                            query += self.__getattribute__(self.lista_atributa[i]).text()
                        if brojac2 < len(self.lista_atributa)-1:
                            query += ", "
                        brojac2 += 1
                    query += ")"
                    print(query)
                    provjeri = True
                    try:
                        parent.csor.execute(query)
                    except mysql.connector.errors.IntegrityError as e:
                        poruka = QtWidgets.QMessageBox()
                        provjeri=False
                        icon = QtGui.QIcon("src/ikonice/logo.jpg")
                        poruka.setWindowIcon(icon)
                        poruka.setWindowTitle("Upozorenje!")
                        poruka.setText("Vec postoji element sa zadatim kljucem!\n"+e.msg)
                        poruka.exec_()
                   
                    except mysql.connector.errors.DataError as e:
                        poruka = QtWidgets.QMessageBox()
                        provjeri=False
                        icon = QtGui.QIcon("src/ikonice/logo.jpg")
                        poruka.setWindowIcon(icon)
                        poruka.setWindowTitle("Upozorenje!")
                        poruka.setText("Uneli ste pogresnu vrednost!\n"+e.msg)
                        poruka.exec_()


                    parent.connection.commit()
                    query = "SELECT * FROM " + self.parent().naziv
                    parent.csor.execute(query)
                    self.parent().table.model().lista_prikaz = []
                    for result in parent.csor.fetchall():
                        lista_podataka = []
                        for i in result:
                            lista_podataka.append(str(i))
                            
                        self.parent().table.model().lista_prikaz.append(GenerickaKlasa(self.lista_atributa, lista_podataka))
               
                    top = QModelIndex()
                    top.child(0,0)
                    bottom = QModelIndex()
                    bottom.child(len(self.parent().table.model().lista_prikaz), self.parent().table.model().broj_kolona)
                    self.parent().table.dataChanged(top, bottom)
                    if provjeri:
                        self.parent().table.model().beginInsertRows(QModelIndex(), 0, 0)
                        model = self.parent().table.model()
                        model.lista_prikaz.append(self.element)
                        self.parent().table.setModel(model)
                        self.parent().table.model().endInsertRows()

                    
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
                self.parent().table.dataChanged(top, bottom) 
                
            elif self.tip == 2:
                self.close()
            
        except ValueError:
            poruka = QtWidgets.QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Pogresna vrednost!")
            poruka.exec_()
            return    
            
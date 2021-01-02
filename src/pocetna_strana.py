
import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QCoreApplication, QEvent, QItemSelectionModel, QPoint
from PySide2.QtGui import QKeyEvent, Qt
from pynput import keyboard
from klase.genericka_klasa import GenerickaKlasa
from left_dock import LeftDock
from PySide2.QtWidgets import QDockWidget, QInputDialog, QMainWindow, QMessageBox, QWidget
from PySide2.QtWidgets import QAbstractItemView
from tab import Tab
from menu_bar import MenuBar
from tool_bar import ToolBar
from klase.metode import *
from klase.prikaz_elementa import PrikazElementa
from PySide2.QtCore import QModelIndex
from pynput.keyboard import Key, Listener
import csv
import os
import json

class PocetnaStrana(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.lista_putanja = []
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.resize(640, 480)
        self.main_window.setWindowTitle("Rukovalac informacionim resursima")
        icon = QtGui.QIcon("src/ikonice/logo.jpg")
        self.main_window.setWindowIcon(icon)

        meni_bar = MenuBar(self.main_window, parent=None)

        self.tool_bar = ToolBar(self.main_window,parent=None)
        self.tool_bar.dodaj.triggered.connect(self.dodavanje_u_datoteku)
        self.tool_bar.izmeni_tabelu.triggered.connect(self.izmena_u_datoteci)
        self.tool_bar.pretrazi.triggered.connect(self.otvori_pretragu)
        self.tool_bar.ukloni_iz_tabele.triggered.connect(self.ukloni_iz_tabele)
        self.tool_bar.spoji_datoteke.triggered.connect(self.spoji_datoteke)
        # self.tool_bar.podeli_datoteku.triggered.connect(self.podeli_datoteke)
        
        status_bar = QtWidgets.QStatusBar()
        #status_bar.showMessage("Prikazan status bar!")
        self.main_window.setStatusBar(status_bar)
        
        self.central_widget = QtWidgets.QTabWidget(self.main_window) 
        # tab = Tab(self.central_widget)
        # self.central_widget.addTab(tab, "Naslov")
        self.central_widget.setTabsClosable(True) 
        self.central_widget.tabCloseRequested.connect(self.delete_tab)
        self.main_window.setCentralWidget(self.central_widget)


        self.dock = LeftDock("dock", parent=None)
        self.main_window.addDockWidget(Qt.LeftDockWidgetArea,self.dock) 
        self.dock.tree.setSelectionMode(QAbstractItemView.SingleSelection) 
        self.dock.tree.clicked.connect(self.read) 
        self.multi_selekt = [] 
        
        self.listener = keyboard.Listener(on_press=self.pritisnuto_dugme, on_release=self.pusteno_dugme) 
        self.listener.start()
        self.main_window.show()

    def podeli_datoteke(self):...

    def spoji_datoteke(self):
        if len(self.multi_selekt) == 0:
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Trenutno nijedna datoteka nije selektovana za spajanje!")
            poruka.exec_()
            return

        kljuc = [2, "broj_indeksa"] #po kom kljucu da sortira, nije zavrseno
        lista = []
        self.multi_selekt.sort()
        
        brojac = 0
        while brojac < len(self.multi_selekt):
            nadjen = False
            for j in range(len(lista)):
                if self.multi_selekt[brojac].row() == lista[j]:
                    nadjen = True
                    break
            if nadjen:
                self.multi_selekt.pop(brojac)
                brojac -= 1
            lista.append(self.multi_selekt[brojac].row())
            brojac += 1

        text, ok = QtWidgets.QInputDialog.getText(None, "Spajanje datoteka", "Unesite ime nove datoteke:", QtWidgets.QLineEdit.Normal, "")
        ime_nove_datoteke = "podaci/podaci/"
        if ok:
            ime_nove_datoteke += str(text) + ".csv"
        
        for i in range(0, len(self.multi_selekt)-1, 2):
            spoji_dve_sekvencijalne_datoteke(
                self.dock.model.filePath(self.multi_selekt[i]),
                self.dock.model.filePath(self.multi_selekt[i+1]),
                kljuc,
                True,
                ime_nove_datoteke)

        self.multi_selekt = []

    def pritisnuto_dugme(self, key):
        if key == Key.ctrl_l:
            self.dock.tree.setSelectionMode(QAbstractItemView.MultiSelection) 

    def pusteno_dugme(self, key):
        if key == Key.ctrl_l:
            self.dock.tree.setSelectionMode(QAbstractItemView.SingleSelection)
            self.multi_selekt = self.dock.tree.selectedIndexes()
            

    def otvori_tabelu_levi_rodjak(self):...
    
    def otvori_tabelu_desni_rodjak(self):...

    def ukloni_iz_tabele(self):
        if self.central_widget.currentWidget() == None:
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Trenutno nijedna datoteka nije otvorena!")
            poruka.exec_()
            return
        
        elif not hasattr(self.central_widget.currentWidget().table, "selected_elem"):
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje")
            poruka.setText("Trenutno nijedan element nije selektovan!")
            poruka.exec_()
            return
            
        model = self.central_widget.currentWidget().table.model()
        element_selected = model.get_element(self.central_widget.currentWidget().table.selected_elem)
        putanja = self.central_widget.currentWidget().meta_podaci[4]
        lista_kljuceva = self.central_widget.currentWidget().meta_podaci[12].split(",")
        lista_atributa = self.central_widget.currentWidget().meta_podaci[5].split(",")
        veze = []
        veze = self.central_widget.currentWidget().meta_podaci[9].split(",")
        
        for i in range(len(veze)):
            if hasattr(self.central_widget.currentWidget(), "sub_table"+str(i+1)):
                if len(self.central_widget.currentWidget().__getattribute__("sub_table"+str(i+1)).model.lista_prikaz) != 0:
                    poruka = QMessageBox()
                    icon = QtGui.QIcon("src/ikonice/logo.jpg")
                    poruka.setWindowIcon(icon)
                    poruka.setWindowTitle("Upozorenje!")
                    poruka.setText("Selektovani element ne sme da se obrise zato sto se njegovi podaci koriste u podtabelama, njegovoj deci!")
                    poruka.exec_()
                    return
        
        self.central_widget.currentWidget().table.model().lista_prikaz = []

        top = QModelIndex()
        top.child(0,0)
        self.central_widget.currentWidget().table.model().beginRemoveRows(top, 0, 0)

        with open(putanja, 'r',newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter = "\n")
            counter = 0
            prva_linija = True
            izbrisan = False
            for row in spamreader:
                if prva_linija:
                    prva_linija = False
                    continue
                if row[0] == "":
                    break
                
                objekat = GenerickaKlasa(lista_atributa, row[0].split(","))
                nadjen = True
                for i in range(len(lista_kljuceva)):
                    if objekat.__getattribute__(lista_kljuceva[i]) != element_selected.__getattribute__(lista_kljuceva[i]):
                        nadjen = False
            
                if not izbrisan and nadjen:
                    izbrisan = True
                    self.central_widget.currentWidget().table.model().removeRow(counter)
                else:
                    self.central_widget.currentWidget().table.model().lista_prikaz.append(objekat)
                counter += 1
        
        self.central_widget.currentWidget().table.model().endRemoveRows()
        
        with open(putanja, 'w', newline='') as f:
            writer = csv.writer(f, delimiter = ",")
            writer.writerow([self.central_widget.currentWidget().putanja_meta])
            for i in range(len(self.central_widget.currentWidget().table.model().lista_prikaz)):
                tekst = ""
                for j in range(len(lista_atributa)):
                    tekst += str(self.central_widget.currentWidget().table.model().lista_prikaz[i].__getattribute__(lista_atributa[j]))
                    if j < len(lista_atributa)-1:
                        tekst += ","
                        
                novi_red = tekst.split(",")
                writer.writerow(novi_red)


    def otvori_tabelu_roditelj(self):
        if self.central_widget.currentWidget() == None:
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Trenutno nijedna datoteka nije otvorena!")
            poruka.exec_()
            return
        elif not hasattr(self.central_widget.currentWidget().table, "selected_elem"):
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Trenutno nijedan element nije selektovan!")
            poruka.exec_()
            return

        model = self.central_widget.currentWidget().table.model()
        element_selected = model.get_element(self.central_widget.currentWidget().table.selected_elem)
        veze = []
        veze = self.central_widget.currentWidget().meta_podaci[9].split(",")
        meta_podaci = self.central_widget.currentWidget().meta_podaci
        lista_kljuceva = []
        brojac = len(veze)-1
        lista_roditelja = []

        for i in range(len(veze)):
            if veze[brojac].find("parent_") == -1:
                veze.pop(brojac)
                brojac -= 1
            else:
                lista_roditelja.append(veze[brojac])
                brojac -= 1
        index = -1

        if len(lista_roditelja) == 0:
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Selektovani element nema roditelja!")
            poruka.exec_()
            return

        elif len(lista_roditelja) > 1:
            list_tuple = ()
            for i in range(len(lista_roditelja)):
                del1 = lista_roditelja[i].find("_")+1
                del2 = lista_roditelja[i].find("(")
                ime = lista_roditelja[i][del1:del2]

                list_tuple = list_tuple + (ime,)

            input = QtWidgets.QInputDialog.getItem(
                self,
                "",
                "Trenutna tabela ima vise od 1 roditelja\nIzaberite roditelja:",
                list_tuple,
                0,
                editable=False)
                
            if input[1]:
                for i in range(len(lista_roditelja)):
                    if lista_roditelja[i].find(input[0]) != -1:
                        index = i
                        break
            else:
                return

        elif len(lista_roditelja) == 1:
            index = 0

        if index == -1:
            return
            
        del1 = lista_roditelja[index].find("_")+1
        lista_roditelja[index] = lista_roditelja[index][del1:len(lista_roditelja[index])]
        del1 = lista_roditelja[index].find("(")
        ime_roditelja = lista_roditelja[index][0:del1]
        nova_putanja = ime_roditelja[0].lower()
        
        for s in range(1, len(ime_roditelja)):
            if ime_roditelja[s].isupper():
                nova_putanja += "_" + ime_roditelja[s].lower()
            else:
                nova_putanja += ime_roditelja[s]
                
        
        nova_putanja = meta_podaci[2] + "\\" + nova_putanja
        if meta_podaci[1] == "serijska":
            nova_putanja += "_ser."
        else:
            nova_putanja += "_sek."
        nova_putanja += meta_podaci[3]
        
        del1 = lista_roditelja[index].find("(") + 1
        del2 = lista_roditelja[index].find(")")
        lista_kljuceva.append(lista_roditelja[index][del1:del2].split("#"))

        tab = Tab(nova_putanja, self.central_widget)
        # self.__getattribute__(ime).clicked.connect(self.element_selected)
        tab.read()
        
        nova_lista = []
        for j in range(len(tab.table.model().lista_prikaz)):
            pronadjen = True
            for m in range(len(lista_kljuceva[len(lista_kljuceva)-1])):
                kljucevi = lista_kljuceva[len(lista_kljuceva)-1][m].split("=")
                if len(kljucevi) == 1:
                    if element_selected.__getattribute__(kljucevi[0]) != tab.table.model().lista_prikaz[j].__getattribute__(kljucevi[0]):
                        pronadjen = False
                elif len(kljucevi) == 2:
                    if element_selected.__getattribute__(kljucevi[0]) != tab.table.model().lista_prikaz[j].__getattribute__(kljucevi[1]):
                        pronadjen = False
                else:
                    print("pocetna_strana.py, 124 linija, eror u len(klucevi):", len(kljucevi), "// ", kljucevi)
            if pronadjen:
                nova_lista.append(tab.table.model().lista_prikaz[j])
        
        if len(nova_lista) == 0:
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Selektovani element nema roditelja sa istim kljucem kao kod selektovanog!")
            poruka.exec_()
            return

        tab.table.model().lista_prikaz = nova_lista

        # tab.table.setModel(tab.table.model())

        tab.btn_down.clicked.connect(self.otvori_tabelu_dete)
        tab.btn_up.clicked.connect(self.otvori_tabelu_roditelj)
        # tab.btn_left.clicked.connect(self.otvori_tabelu_levi_rodjak)
        # tab.btn_right.clicked.connect(self.otvori_tabelu_desni_rodjak)

        self.central_widget.removeTab(self.central_widget.currentIndex())
        self.central_widget.addTab(tab, ime_roditelja)

        meta = ""
        for s in range(len(self.central_widget.currentWidget().meta_podaci[0])):
            if self.central_widget.currentWidget().meta_podaci[0][s].isupper():
                meta += "_" + self.central_widget.currentWidget().meta_podaci[0][s].lower()
            else:
                meta += self.central_widget.currentWidget().meta_podaci[0][s]
                
        meta = meta[1:len(meta)]
        meta = self.central_widget.currentWidget().meta_podaci[2] + "\\" + meta
        if self.central_widget.currentWidget().meta_podaci[1] == "serijska":
            meta += "_ser."
        else:
            meta += "_sek."
        meta += self.central_widget.currentWidget().meta_podaci[3]
        
        self.lista_putanja.append(meta)
        self.lista_putanja.remove(self.lista_putanja[self.central_widget.currentIndex()])

    def otvori_tabelu_dete(self):
        if self.central_widget.currentWidget() == None:
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Trenutno nijedna datoteka nije otvorena!")
            poruka.exec_()
            return
        elif not hasattr(self.central_widget.currentWidget().table, "selected_elem"):
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Trenutno nijedan element nije selektovan!")
            poruka.exec_()
            return
        elif self.central_widget.currentWidget().tab_widget.currentWidget() == None:
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Selektovani element nema podtabele!")
            poruka.exec_()
            return
        elif len(self.central_widget.currentWidget().tab_widget.currentWidget().model.lista_prikaz) == 0:
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Selektovani element nema decu u selektovanoj podtabeli!")
            poruka.exec_()
            return

        child = self.central_widget.currentWidget().tab_widget.currentWidget()
        tab = Tab(child.putanja, self.central_widget)
        tab.read()
        tab.table.model().lista_prikaz = child.model.lista_prikaz
        
        tab.btn_down.clicked.connect(self.otvori_tabelu_dete)
        tab.btn_up.clicked.connect(self.otvori_tabelu_roditelj)

        self.central_widget.removeTab(self.central_widget.currentIndex())
        self.central_widget.addTab(tab, child.meta_podaci[0])

        meta = ""
        for s in range(len(child.meta_podaci[0])):
            if child.meta_podaci[0][s].isupper():
                meta += "_" + child.meta_podaci[0][s].lower()
            else:
                meta += child.meta_podaci[0][s]
                
        meta = meta[1:len(meta)]
        meta = child.meta_podaci[2] + "\\" + meta
        if child.meta_podaci[1] == "serijska":
            meta += "_ser."
        else:
            meta += "_sek."
        meta += child.meta_podaci[3]

        self.lista_putanja.append(meta)
        self.lista_putanja.remove(self.lista_putanja[self.central_widget.currentIndex()])

    def izmena_u_datoteci(self):
        if self.central_widget.currentWidget() == None:
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Trenutno nijedna datoteka nije otvorena!")
            poruka.exec_()
            return
        elif not hasattr(self.central_widget.currentWidget().table, "selected_elem"):
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Trenutno nijedan element nije selektovan!")
            poruka.exec_()
            return
            
        model = self.central_widget.currentWidget().table.model()
        selektovani_element = model.get_element(self.central_widget.currentWidget().table.selected_elem)
        prikaz = PrikazElementa(self.central_widget.currentWidget(),
                self.central_widget.currentWidget().meta_podaci,False, selektovani_element)
    
        prikaz.exec_()

    def dodavanje_u_datoteku(self):
        if self.central_widget.currentWidget() == None:
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Trenutno nijedna datoteka nije otvorena!")
            poruka.exec_()
            return
            
        prikaz = PrikazElementa(self.central_widget.currentWidget(),
                self.central_widget.currentWidget().meta_podaci)
    
        prikaz.exec_()

    def otvori_pretragu(self):
        if self.central_widget.currentWidget() == None:
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Trenutno nijedna datoteka nije otvorena!")
            poruka.exec_()
            return

        prikaz = PrikazElementa(self.central_widget.currentWidget(), self.central_widget.currentWidget().meta_podaci,True)
        prikaz.exec_()
        if len(prikaz.lista_atr) != 0 and len(prikaz.lista_kriterijuma) != 0:
            model = self.central_widget.currentWidget().table.model()
            model = pretraga(
                prikaz.lista_atr, prikaz.lista_kriterijuma,
                prikaz.lista_vece_manje, 
                self.central_widget.currentWidget().meta_podaci)

            if len(model.lista_prikaz) == 0:
                poruka = QMessageBox()
                icon = QtGui.QIcon("src/ikonice/logo.jpg")
                poruka.setWindowIcon(icon)
                poruka.setWindowTitle("Upozorenje!")
                poruka.setText("Zadata pretraga nije pronasla vrednosti koje odgovaraju zadatim kriterijumima.")
                poruka.exec_()
                return

            self.central_widget.currentWidget().table.setModel(model)
        else:
            poruka = QMessageBox()
            icon = QtGui.QIcon("src/ikonice/logo.jpg")
            poruka.setWindowIcon(icon)
            poruka.setWindowTitle("Upozorenje!")
            poruka.setText("Niste zadali ni jedan kriterijum za pretragu, pretraga je prekinuta.")
            poruka.exec_()
            return

    def delete_tab(self, index):
        self.central_widget.setCurrentIndex(index)
        tab = self.central_widget.currentWidget()
        
        if hasattr(tab, "sortirano") and len(tab.table.model().lista_prikaz) > 1:
            if tab.meta_podaci[1] == "serijska": 
                while True:
                    izabrano = -1
                    list_tuple = ()
                    lista = ["Samo stare podatke", "Samo nove podatke", "Ili i stare i nove podatke"]
                    for i in range(len(lista)):
                        list_tuple = list_tuple + (lista[i],)

                    input = QtWidgets.QInputDialog.getItem(
                        tab,
                        "",
                        "Posto ste sortirali tabelu\nIzaberite da li zelite da sacuvate:",
                        list_tuple,
                        0,
                        editable=False)
                        
                    if input[1]:
                        for i in range(len(lista)):
                            if lista[i].find(input[0]) != -1:
                                izabrano = i
                                break
                        break

                putanja = tab.meta_podaci[4]

                if izabrano == 2:
                    i = 0
                    while True:
                        del1 = tab.meta_podaci[4].rfind(".")
                        deo = tab.meta_podaci[4][0:del1]
                        nastavak = tab.meta_podaci[4][del1:len(tab.meta_podaci[4])]
                        if not os.path.exists(deo + "_new"+str(i+1) + nastavak):
                            putanja = deo + "_new"+str(i+1) + nastavak
                            break
                        i += 1

                if izabrano != 0:
                    with open(putanja, 'w', newline='') as f:
                        writer = csv.writer(f, delimiter = ",")
                        writer.writerow([tab.putanja_meta])
                        for i in range(len(tab.table.model().lista_prikaz)):
                            tekst = ""
                            for j in range(len(tab.table.model().nazivi_atributa)):
                                tekst += str(tab.table.model().lista_prikaz[i].__getattribute__(tab.table.model().nazivi_atributa[j]))
                                if j < len(tab.table.model().nazivi_atributa)-1:
                                    tekst += ","
                                
                            novi_red = tekst.split(",")
                            writer.writerow(novi_red)

        self.central_widget.removeTab(index)
        self.lista_putanja.remove(self.lista_putanja[index])

    def read(self, index):
        putanja = self.dock.model.filePath(index)
        ista_putanja = False
        for i in range(len(self.lista_putanja)):
            if putanja == self.lista_putanja[i]:
                ista_putanja = True
                return
        if not ista_putanja:
            self.lista_putanja.append(putanja)

            tab = Tab(putanja, self.central_widget)
            tab.read()
            tab.btn_down.clicked.connect(self.otvori_tabelu_dete)
            tab.btn_up.clicked.connect(self.otvori_tabelu_roditelj)
            self.central_widget.addTab(tab, tab.meta_podaci[0])
            self.central_widget.setCurrentIndex(self.central_widget.currentIndex()+1)
            
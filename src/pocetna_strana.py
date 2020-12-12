
import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QPoint
from PySide2.QtGui import Qt
from left_dock import LeftDock
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QAbstractItemView
from tab import Tab
from menu_bar import MenuBar
from tool_bar import ToolBar
from klase.metode import citanje_meta_podataka
from klase.metode import pretraga_serijske
from klase.metode import kreiraj_model
from klase.prikaz_elementa import PrikazElementa
from PySide2.QtCore import QModelIndex
import csv
import json


class PocetnaStrana:
    def __init__(self):
        super().__init__()
        self.lista_putanja = []
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.resize(640, 480)
        self.main_window.setWindowTitle("Rukovalac informacionim resursima")
        icon = QtGui.QIcon("src/ikonice/logo.jpg")
        self.main_window.setWindowIcon(icon)

        meni_bar = MenuBar(self.main_window, parent=None)

        self.tool_bar = ToolBar(self.main_window,parent=None)
        self.tool_bar.dodaj.triggered.connect(self.otvori_prikaz)
        self.tool_bar.pretrazi.triggered.connect(self.otvori_pretragu)
        status_bar = QtWidgets.QStatusBar()
        status_bar.showMessage("Prikazan status bar!")
        self.main_window.setStatusBar(status_bar)
        
        self.central_widget = QtWidgets.QTabWidget(self.main_window)
        # tab = Tab(self.central_widget)
        # self.central_widget.addTab(tab, "Naslov")
        self.central_widget.setTabsClosable(True)
        self.central_widget.tabCloseRequested.connect(self.delete_tab)
        self.main_window.setCentralWidget(self.central_widget)


        self.dock = LeftDock("dock", parent=None)
        self.main_window.addDockWidget(Qt.LeftDockWidgetArea,self.dock)
        self.dock.tree.clicked.connect(self.read)
        
        self.main_window.show()

    def otvori_tabelu_roditelj(self):
        if not hasattr(self.central_widget.currentWidget().table, "selected_elem"):
            return

        model = self.central_widget.currentWidget().table.model()
        element_selected = model.get_element(self.central_widget.currentWidget().table.selected_elem)
        veze = []
        veze = self.central_widget.currentWidget().meta_podaci[9].split(",")
        meta_podaci = self.central_widget.currentWidget().meta_podaci
        lista_kljuceva = []
        counter = len(veze)-1
        lista_roditelja = []

        for i in range(len(veze)):
            if veze[counter].rfind("parent_") == -1:
                veze.pop(counter)
                counter -= 1
            else:
                lista_roditelja.append(veze[counter])
        index = -1
        if len(lista_roditelja) == 0:...
            # poruka da tabela nema roditelja
            # i return
        elif len(lista_roditelja) > 1:...
            # index = dialog drop down lista da izabere kog roditelja zeli
            #  iz liste_roditelja i sacuvati index u index
        elif len(lista_roditelja) == 1:
            index = 0

        if index == -1:
            return
            
        del1 = lista_roditelja[index].find("_")+1
        lista_roditelja[index] = lista_roditelja[index][del1:len(lista_roditelja[index])]
        del1 = lista_roditelja[index].find("(")
        ime_roditelja = lista_roditelja[index][0:del1]
        nova_meta = ""
        for s in range(len(ime_roditelja)):
            if ime_roditelja[s].isupper():
                nova_meta += "_" + ime_roditelja[s].lower()
            else:
                nova_meta += ime_roditelja[s]

        nova_meta = nova_meta[1:len(nova_meta)]
        nova_meta = meta_podaci[2] + "\\metaPodaci\\" + nova_meta + "_meta_podaci." + meta_podaci[3]
        
        del1 = lista_roditelja[index].find("(") + 1
        del2 = lista_roditelja[index].find(")")
        lista_kljuceva.append(lista_roditelja[index][del1:del2].split("#"))

        tab = Tab(self.central_widget)
        # self.__getattribute__(ime).clicked.connect(self.element_selected)
        lista = citanje_meta_podataka(nova_meta)
        tab.read(lista)
        
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

        tab.table.model().lista_prikaz = nova_lista

        tab.table.setModel(tab.table.model())

        tab.btn_down.clicked.connect(self.otvori_tabelu_dete)
        tab.btn_up.clicked.connect(self.otvori_tabelu_roditelj)
        self.central_widget.removeTab(self.central_widget.currentIndex())
        self.central_widget.addTab(tab, ime_roditelja)

    def otvori_tabelu_dete(self):
        if self.central_widget.currentWidget().tab_widget.currentWidget() == None:
            return
        child = self.central_widget.currentWidget().tab_widget.currentWidget()
        tab = Tab(self.central_widget)
        tab.read(child.meta_podaci)
        tab.btn_down.clicked.connect(self.otvori_tabelu_dete)
        tab.btn_up.clicked.connect(self.otvori_tabelu_roditelj)
        self.central_widget.removeTab(self.central_widget.currentIndex())
        self.central_widget.addTab(tab, child.meta_podaci[0])

    def otvori_prikaz(self):
        if self.central_widget.currentWidget() == None:
            return
        self.prikaz = PrikazElementa(self.central_widget.currentWidget(),
                    self.central_widget.currentWidget().meta_podaci[5].split(","))
    
    
    def otvori_pretragu(self):
        if self.central_widget.currentWidget() == None:
            return
        lista_atributa = self.central_widget.currentWidget().meta_podaci[5].split(",")
        self.prikaz = PrikazElementa(self.central_widget.currentWidget(), lista_atributa)
        lista_kljuceva = self.prikaz.lista_atr
        lista_kriterijuma = self.prikaz.lista_kriterijuma

        self.central_widget.currentWidget().model = pretraga_serijske(
            lista_kljuceva, lista_kriterijuma, 
            self.central_widget.currentWidget().meta_podaci)

        self.central_widget.currentWidget().table.setModel(self.central_widget.currentWidget().model)

    def delete_tab(self, index):
        self.central_widget.removeTab(index)
        self.lista_putanja.remove(self.lista_putanja[index])

    def read(self, index):
        putanja = self.dock.model.filePath(index)
        ista_putanja = False
        for i in range(len(self.lista_putanja)):
            if putanja == self.lista_putanja[i]:
                ista_putanja = True
        if not ista_putanja:
            self.lista_putanja.append(putanja)
            neka_lista = citanje_meta_podataka(putanja)

            tab = Tab(self.central_widget)
            tab.read(neka_lista)
            tab.btn_down.clicked.connect(self.otvori_tabelu_dete)
            tab.btn_up.clicked.connect(self.otvori_tabelu_roditelj)
            self.central_widget.addTab(tab, neka_lista[0])
            
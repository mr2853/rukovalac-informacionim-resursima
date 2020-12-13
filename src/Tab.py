from os import linesep
from PySide2 import QtWidgets, QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import QAbstractItemView
from klase.model import Model
from PySide2.QtWidgets import QWidget
from PySide2 import QtGui
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QHeaderView
from PySide2.QtCore import QModelIndex
from PySide2.QtCore import QObject, Signal, Slot
from klase.metode import citanje_meta_podataka, kreiraj_model
import json
from klase.genericka_klasa import GenerickaKlasa

class Tab(QtWidgets.QWidget):
    def __init__(self, putanja, parent=None):
        super().__init__(parent)
        self.putanja_meta_podaci = putanja
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_sub_tab)

        self.table = QtWidgets.QTableView(self.tab_widget)
        
        self.table.setUpdatesEnabled(True)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.clicked.connect(self.element_selected)

        self.sub_layout = QtWidgets.QHBoxLayout()

        self.btn_up = QtWidgets.QPushButton("↑", self)
        self.btn_down = QtWidgets.QPushButton("↓", self)
        self.btn_left = QtWidgets.QPushButton("<", self)
        self.btn_right = QtWidgets.QPushButton(">", self)

        self.btn_up.setFixedSize(50,80)
        self.btn_down.setFixedSize(50,80)
        self.btn_left.setFixedSize(50,80)
        self.btn_right.setFixedSize(50,80)

        self.sub_layout.addStretch()

        self.sub_layout.addWidget(self.btn_up)
        self.sub_layout.addWidget(self.btn_down)
        self.sub_layout.addWidget(self.btn_left)
        self.sub_layout.addWidget(self.btn_right)
        self.sub_layout.addStretch()
        self.sub_layout.setSpacing(0)

        self.main_layout.addWidget(self.table)
        self.main_layout.addLayout(self.sub_layout)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def delete_tab(self, index):
        self.main_layout.removeWidget(index)

    def delete_sub_tab(self, index):
        self.tab_widget.removeTab(index)
    
    def read(self, lista):
        self.model = kreiraj_model(lista)
        self.meta_podaci = lista

        self.table.setModel(self.model)
        self.table.setSortingEnabled(True)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.horizontalHeader().sectionClicked.connect(self.sort_table) # kada se klikne na neki horizontalHeader da pozove self.sort_table
        if lista[1] == "sekvencijalna":
            self.sort_table(0)
            self.model.upisan_podatak.connect(self.sort_table) # u slucaju izmene podataka da pozove sort_table

    
    def sort_table(self, index):
        """
        sortira listu
        :param: index - oznacava po kojoj koloni/atributu se sortira
        """
        index = self.table.horizontalHeader().sortIndicatorSection() # dobavljamo vrednost selektovanog headera
        nacin_sortiranja = self.table.horizontalHeader().sortIndicatorOrder() # dobavljamo koja vrednost sortiranja je oznacena
        self.table.sortByColumn(index, nacin_sortiranja)
        if nacin_sortiranja == Qt.AscendingOrder: # ako je prema vecem
            self.model.sort_list(index, False)
        else:                                   # ako nije prema vecem nego prema manjem
            self.model.sort_list(index, True)
        
        top = QModelIndex()
        top.child(0,0)
        bottom = QModelIndex()
        bottom.child(len(self.model.lista_prikaz), self.model.broj_kolona)
        self.table.dataChanged(top, bottom) # da refresuje tabelu od top indexa to bottom indexa
    
    def element_selected(self, index):
        self.table.selected_elem = index
        model = self.table.model()
        element_selected = model.get_element(index)
        self.tab_widget.clear()
        self.meta_putanje_dece = []
        imena_dece = []
        lista_kljuceva = []
        veze = []
        veze = self.meta_podaci[9].split(",")
        counter = len(veze)-1

        for i in range(len(veze)):
            if veze[counter].rfind("child_") == -1:
                veze.pop(counter)
                counter -= 1
            else:
                del1 = veze[counter].find("_")+1
                veze[counter] = veze[counter][del1:len(veze[counter])]
                del1 = veze[counter].find("(")
                ime_deteta = veze[counter][0:del1]
                imena_dece.append(ime_deteta)
                nova_meta = ""
                for s in range(len(ime_deteta)):
                    if ime_deteta[s].isupper():
                        nova_meta += "_" + ime_deteta[s].lower()
                    else:
                        nova_meta += ime_deteta[s]

                nova_meta = nova_meta[1:len(nova_meta)]
                nova_meta = self.meta_podaci[2] + "\\metaPodaci\\" + nova_meta + "_meta_podaci." + self.meta_podaci[3]
                self.meta_putanje_dece.append(nova_meta)
                # nadjeno = False
                # for m in range(len(self.meta_putanje_dece)):
                #     if self.meta_putanje_dece[m] == nova_meta:
                #         nadjeno = True
                # if nadjeno:
                #     return
                
                del1 = veze[counter].find("(") + 1
                del2 = veze[counter].find(")")
                lista_kljuceva.append(veze[counter][del1:del2].split("#"))

        
        
                ime = "sub_table" + str(i+1)
                self.__setattr__(ime, QtWidgets.QTableView(self.tab_widget))
                self.__getattribute__(ime).setSelectionMode(QAbstractItemView.SingleSelection)
                self.__getattribute__(ime).setSelectionBehavior(QAbstractItemView.SelectRows)
                # self.__getattribute__(ime).clicked.connect(self.element_selected)
                lista = citanje_meta_podataka(nova_meta)
                self.__getattribute__(ime).model = kreiraj_model(lista)
                self.__getattribute__(ime).meta_podaci = lista
                
                nova_lista = []
                for j in range(len(self.__getattribute__(ime).model.lista_prikaz)):
                    pronadjen = True
                    for m in range(len(lista_kljuceva[len(lista_kljuceva)-1])):
                        kljucevi = lista_kljuceva[len(lista_kljuceva)-1][m].split("=")
                        if len(kljucevi) == 1:
                            if element_selected.__getattribute__(kljucevi[0]) != self.__getattribute__(ime).model.lista_prikaz[j].__getattribute__(kljucevi[0]):
                                pronadjen = False
                        elif len(kljucevi) == 2:
                            if element_selected.__getattribute__(kljucevi[0]) != self.__getattribute__(ime).model.lista_prikaz[j].__getattribute__(kljucevi[1]):
                                pronadjen = False
                        else:
                            print("tab.py, 135 linija, eror u len(klucevi):", len(kljucevi), "// ", kljucevi)
                    if pronadjen:
                        nova_lista.append(self.__getattribute__(ime).model.lista_prikaz[j])

                self.__getattribute__(ime).model.lista_prikaz = nova_lista

                self.__getattribute__(ime).setModel(self.__getattribute__(ime).model)
            
                self.tab_widget.addTab(self.__getattribute__(ime), ime_deteta)
                counter -= 1
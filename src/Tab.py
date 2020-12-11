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
import json
from klase.genericka_klasa import GenerickaKlasa

class Tab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()
        self.table = QtWidgets.QTableView(self.tab_widget)
        
        self.table.setUpdatesEnabled(True)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.clicked.connect(self.element_selected)
        self.main_layout.addWidget(self.table)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.main_layout.removeWidget(index)
    
    def read(self, lista):
        self.model = Model(lista)
        with open(lista[4], newline='\n') as f:
            while True:
                podaci = f.readline().strip()
                if podaci == "":
                    break
                
                lista_podataka = podaci.split(",")
                self.meta_podaci = lista
                self.model.lista_original.append(GenerickaKlasa(lista[5].split(","), lista_podataka))
                self.model.lista_prikaz.append(GenerickaKlasa(lista[5].split(","), lista_podataka))

        self.table.setModel(self.model)
        self.table.setSortingEnabled(True)
        self.table.sortByColumn(0,Qt.AscendingOrder)
        self.table.horizontalHeader().sectionClicked.connect(self.sort_table) # kada se klikne na neki horizontalHeader da pozove self.sort_table
        if lista[1] == "sekvencijalna":
            self.model.upisan_podatak.connect(self.sort_table) # u slucaju izmene podataka da pozove sort_table

    @Slot(int)
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
        model = self.table.model()
        element_selected = model.get_element(index)
        # veze = []
        # veze = self.meta_podaci[9].split(",")
        # for i in veze:
        #     if not i.find("child_"):
        #         veze.pop(i)
        #     else:
        #         del1 = veze[i].find("_")+1
        #         veze[i] = veze[i][del1:len(veze[i])]
        #         del1 = veze[i].find("(")
        #         ime_deteta = veze[i][0:del1]
        #         ime_deteta = ime_deteta.lower()
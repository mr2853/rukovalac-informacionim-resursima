from os import linesep
from PySide2 import QtWidgets, QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import QAbstractItemView
from klase.model import Model
from klase.student import Student
from klase.visokoskolska_ustanova import VisokoskolskaUstanova
from klase.tok_studija import TokStudija
from klase.studijski_programi import StudijskiProgrami
from klase.predmet import Predmet
from klase.plan_studijske_grupe import PlanStudijskeGrupe
from klase.nivo_studija import NivoStudija
from PySide2.QtWidgets import QWidget
from PySide2 import QtGui
from PySide2 import QtCore
from PySide2.QtCore import Qt
from PySide2.QtWidgets import QHeaderView
from PySide2.QtCore import QModelIndex
from PySide2.QtCore import QObject, Signal, Slot
import json

class Tab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.table = QtWidgets.QTableView()
        self.table.setUpdatesEnabled(True)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.main_layout.addWidget(self.table)
        self.setLayout(self.main_layout)

    def delete_tab(self, index):
        self.main_layout.removeWidget(index)
    
    def read(self, lista_json):
        self.model = Model(lista_json["nazivi_atributa"], lista_json["nazivi_kolona"])
        with open(lista_json["podaci"], newline='\n') as f:
            while True:
                podaci = f.readline().strip()
                if podaci == "":
                    break
                
                lista_podataka = podaci.split(",")
                self.model.lista_original.append(globals()[lista_json["klasa"]](lista_podataka))
                self.model.lista_prikaz.append(globals()[lista_json["klasa"]](lista_podataka))

        self.table.setModel(self.model)
        self.table.setSortingEnabled(True)
        self.table.sortByColumn(0,Qt.AscendingOrder)
        self.table.horizontalHeader().sectionClicked.connect(self.sort_table) # kada se klikne na neki horizontalHeader da pozove self.sort_table
        self.model.upisan_podatak.connect(self.sort_table) # u slucaju izmene podataka da pozove sort_table
        self.sort_table(0) # pri ucitavanju datoteke sortiramo tabelu prema prvoj koloni

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

    # def element_selected(self, index):
        # model = self.table.model()
        # element_selected = model.get_element(index)
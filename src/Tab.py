from PySide2 import QtWidgets, QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import QAbstractItemView
from klase.model import Model
from klase.student import Student
from PySide2.QtWidgets import QWidget
from PySide2 import QtGui
import json

class Tab(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()
        self.table = QtWidgets.QTableView(self.tab_widget)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        # self.table.clicked.connect(self.student_selected)
        self.main_layout.addWidget(self.table)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)
        
    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)
    
    def open(self):
        self.tab_widget1.setWindowTitle("neki naslov")
    
    def read(self, lista_json):
        model = Model(lista_json["nazivi_atributa"], lista_json["nazivi_kolona"])
        with open(lista_json["podaci"]) as f:
            while True:
                podaci = f.readline()
                if podaci == "":
                    break
                lista_podataka = podaci.split(",")
                model.lista.append(globals()[lista_json["klasa"]](lista_podataka))
                
        self.table.setModel(model)
    
    # def student_selected(self, index):
        # model = self.table.model()
        # selected_student = model.get_element(index)
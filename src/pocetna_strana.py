import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QPoint
from PySide2.QtGui import Qt
from left_dock import LeftDock
from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget
from tab import Tab
from menu_bar import MenuBar
from tool_bar import ToolBar
from klase.metode import citanje_meta_podataka
from klase.prikaz_elementa import PrikazElementa
import csv
import json


class PocetnaStrana:
    def __init__(self):
        super().__init__()
        self.lista_putanja = []
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.resize(640, 480)
        self.main_window.setWindowTitle("Rukovalac informacionim resursima")
        icon = QtGui.QIcon("ikonice/logo.jpg")
        self.main_window.setWindowIcon(icon)

        meni_bar = MenuBar(self.main_window, parent=None)

        self.tool_bar = ToolBar(self.main_window,parent=None)
        self.tool_bar.create_o.triggered.connect(self.otvori_prikaz)
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
    def otvori_prikaz(self):
        self.prikaz = PrikazElementa(self.central_widget.currentWidget(),
                    self.central_widget.currentWidget().meta_podaci[5].split(","))
    
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
            self.central_widget.addTab(tab, putanja.split("/")[-1])
            tab.read(neka_lista)
            
import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtCore import QPoint
from PySide2.QtGui import Qt
from left_dock import LeftDock
from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget
from tab import Tab
from menu_bar import MenuBar
import csv
import json


class PocetnaStrana:
    def __init__(self):
        super().__init__()
        self.lista_putanja = []
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.resize(640, 480)
        self.main_window.setWindowTitle("Rukovalac informacionim resursima")
        icon = QtGui.QIcon("icons8-edit-file-64.png")
        self.main_window.setWindowIcon(icon)

        meni_bar = MenuBar(self.main_window, parent=None)
        

        toolbar = QtWidgets.QToolBar("tool bar", parent=None)
        self.main_window.addToolBar(toolbar)

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

    def save(self):
        print("kao sacuvan")

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
            neka_lista = []
            with open(putanja, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter = "\n")
                counter = 0
                for row in spamreader:
                    dve_tacke = row[0].find(":")+1
                    row[0] = row[0][dve_tacke:len(row[0])]

                    if counter == 4:
                        del1 = row[0].find("\\")
                        del2 = row[0].find(".") + 1
                        row[0] = row[0][del1:del2]
                        row[0] = neka_lista[2] + row[0] + neka_lista[3]
                        
                    neka_lista.append(row[0])
                    counter += 1

            tab1 = Tab(self.central_widget)
            self.central_widget.addTab(tab1, putanja.split("/")[-1])
            tab1.read(neka_lista)
            
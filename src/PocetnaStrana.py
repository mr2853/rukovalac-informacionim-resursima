import sys
from PySide2 import QtWidgets, QtGui
from PySide2.QtGui import Qt
from LeftDock import LeftDock
from PySide2 import QtWidgets
from PySide2.QtWidgets import QWidget
from CentralniWidget import CentralniWidget
from Tab import Tab
from MenuBar import MenuBar
from klase.Student import Student


class PocetnaStrana:
    def __init__(self):
        super().__init__()
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.resize(640, 480)
        self.main_window.setWindowTitle("Rukovalac informacionim resursima")
        icon = QtGui.QIcon("icons8-edit-file-64.png")
        self.main_window.setWindowIcon(icon)

        meni_bar = MenuBar(self.main_window, parent=None)
        toolbar = QtWidgets.QToolBar("tool bar", parent=None)
        self.main_window.addToolBar(toolbar)

        statusBar = QtWidgets.QStatusBar()
        statusBar.showMessage("Prikazan status bar!")
        self.main_window.setStatusBar(statusBar)
        
        self.central_widget = QtWidgets.QTabWidget(self.main_window)
        tab = Tab(self.central_widget)
        self.central_widget.addTab(tab, "Naslov")
        self.central_widget.setTabsClosable(True)
        self.central_widget.tabCloseRequested.connect(self.delete_tab)
        self.main_window.setCentralWidget(self.central_widget)


        self.dock = LeftDock("dock", parent=None)
        self.main_window.addDockWidget(Qt.LeftDockWidgetArea,self.dock)
        self.dock.tree.clicked.connect(self.read)
        
        self.main_window.show()
    
    def delete_tab(self, index):
        self.central_widget.removeTab(index)

    def read(self, index):
        path = self.dock.model.filePath(index)
        with open(path) as f:
            text = (f.read())
            tab1 = Tab(self.central_widget)
            self.central_widget.addTab(tab1, path.split("/")[-1])
            tab1.read(text)
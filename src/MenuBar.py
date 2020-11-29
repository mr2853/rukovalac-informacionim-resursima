from PySide2 import QtWidgets
from PySide2 import QtWidgets
class MenuBar(QtWidgets.QMenuBar):
    def __init__(self, main, parent):
        super().__init__(parent)
        self.menu_bar = QtWidgets.QMenuBar(parent=None)
        self.qmenu1 = QtWidgets.QMenu("File",parent=None)
        self.qmenu2 = QtWidgets.QMenu("Edit",parent=None)
        self.qmenu3 = QtWidgets.QMenu("View",parent=None)
        self.qmenu4 = QtWidgets.QMenu("Help",parent=None)

        self.sub_menu1 = self.qmenu1.addMenu("Prva opcija")
        self.sub_menu2 = self.qmenu1.addAction("Druga opcija")
        self.sub_menu3 = self.qmenu1.addAction("Treca opcija")
        self.sub_menu4 = self.qmenu1.addMenu("Cetvrta opcija")

        self.sub_menu1.addAction("Prva opcija")
        self.sub_menu1.addAction("Druga opcija")

        self.sub_menu4.addAction("Prva opcija")
        self.sub_menu4.addAction("Druga opcija")
        self.sub_menu4.addAction("Treca opcija")
        self.sub_menu4.addAction("Cetvrta opcija")

        self.qmenu2.addAction("Prva opcija")
        self.qmenu2.addAction("Druga opcija")
        self.qmenu2.addAction("Treca opcija")
        self.qmenu2.addAction("Cetvrta opcija")

        self.qmenu3.addAction("Prva opcija")
        self.qmenu3.addAction("Druga opcija")
        self.qmenu3.addAction("Treca opcija")
        self.qmenu3.addAction("Cetvrta opcija")

        self.qmenu4.addAction("Prva opcija")
        self.qmenu4.addAction("Druga opcija")
        self.qmenu4.addAction("Treca opcija")
        self.qmenu4.addAction("Cetvrta opcija")

        self.qMenuBar = QtWidgets.QMenuBar()
        self.qMenuBar.addMenu(self.qmenu1)
        self.qMenuBar.addMenu(self.qmenu2)
        self.qMenuBar.addMenu(self.qmenu3)
        self.qMenuBar.addMenu(self.qmenu4)

        self.menu_bar.addMenu(self.qmenu1)
        self.menu_bar.addMenu(self.qmenu2)
        self.menu_bar.addMenu(self.qmenu3)
        self.menu_bar.addMenu(self.qmenu4)

        main.setMenuBar(self.menu_bar)
from PySide2 import QtWidgets
from PySide2 import QtGui
class MenuBar(QtWidgets.QMenuBar):
    def __init__(self, main, parent):
        super().__init__(parent)
        self.menu_bar = QtWidgets.QMenuBar(parent=None)
        self.qmenu1 = QtWidgets.QMenu("File",parent=None)
        self.qmenu2 = QtWidgets.QMenu("Edit",parent=None)
        self.qmenu3 = QtWidgets.QMenu("Help",parent=None)

       
        self.qmenu1.addAction(QtGui.QIcon("about.png"), "O aplikaciji")
        
        self.qmenu2.addAction(QtGui.QIcon("ikonice/copy.png"),"Copy")
        self.qmenu2.addAction(QtGui.QIcon("ikonice/paste.png"),"Paste")
        

        self.qmenu3.addAction(QtGui.QIcon("ikonice/upustvo.png"),"Korisnicko upustvo")
      
        self.qMenuBar = QtWidgets.QMenuBar()
        self.qMenuBar.addMenu(self.qmenu1)
        self.qMenuBar.addMenu(self.qmenu2)
        self.qMenuBar.addMenu(self.qmenu3)
     

        self.menu_bar.addMenu(self.qmenu1)
        self.menu_bar.addMenu(self.qmenu2)
        self.menu_bar.addMenu(self.qmenu3)

    

        main.setMenuBar(self.menu_bar)
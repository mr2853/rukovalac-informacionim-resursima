from PySide2 import QtWidgets, QtCore
from PySide2 import QtWidgets
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import QStyleOptionViewItem

class LeftDock(QtWidgets.QDockWidget):
    kliknut = QtCore.Signal(str) #signal se emituje kada se neki dogadjaj desi, slot je funkcija koja je pozvana kao odgovor na signal
    def __init__(self, title, parent):
        super().__init__(title, parent)

        self.model = QtWidgets.QFileSystemModel() #klasa koja nam obezbjedjuje pristup lokalnim fajlovima, obezbjedjuje funkcije za preimenovanje i uklanjanje datotek i direktorijuma kao i kreiranje novih
        self.model.setRootPath("podaci\\podaci") # sa ovim povezujemo direktorijume
        self.setFeatures(self.DockWidgetFeature.NoDockWidgetFeatures)
        self.tree = QtWidgets.QTreeView() #treeView koristimo da nam se prikaze sadrzaj modela
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index("podaci\\podaci")) #The view's root index can be used to control how much of a hierarchical model is displayed.
        self.tree.hideColumn(1) #sakrivanje druge, trece i cetvrte kolone gdje se prikazuju podaci
        self.tree.hideColumn(2)
        self.tree.hideColumn(3)
        # self.tree.setColumnWidth(0,250)
        self.tree.setRowHidden(0, self.tree.rootIndex(), True) #If hide is true row will be hidden, otherwise it will be shown.
        self.tree.clicked.connect(self.file_clicked)
        self.setWidget(self.tree)

    def file_clicked(self, index): # funkcija kada je neki fajl kliknut
        path = self.model.filePath(index)
        print(path) #ovo stampa putanju onoga na sto smo kliknuli apsolutnu
        self.kliknut.emit(path)
        
    # def change(self):
    #     paint = QPainter()
    #     style = QStyleOptionViewItem()
    #     style.WrapText = "neki tekst"
    #     index = QtCore.QModelIndex()
    #     index.child(0,0)
    #     self.tree.drawRow(paint, style, index)
    #     paint.drawText = "da"
    
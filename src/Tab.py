from PySide2 import QtWidgets, QtGui
from PySide2 import QtWidgets

class Tab(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()
        self.table = QtWidgets.QTableWidget(3, 3, self)
        self.setVerticalHeader(self.table)
        self.main_layout.addWidget(self.table)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def setVerticalHeader(self, table):
        for i in range(table.rowCount()):
            self.table.setVerticalHeaderItem(i+1, QtWidgets.QTableWidgetItem(str(i)))
    
    def setHorizontalHeaderItem(self, index, text):
        self.table.setHorizontalHeaderItem(index, QtWidgets.QTableWidgetItem(str(text)))

    def show_tabs(self):
        self.tab_widget.addTab(QtWidgets.QTableWidget(5, 5, self.tab_widget), QtGui.QIcon("icons8-edit-file-64.png"), "Prva Podtabela")
        self.tab_widget.addTab(QtWidgets.QTableWidget(5, 5, self.tab_widget), QtGui.QIcon("icons8-edit-file-64.png"), "Druga Podtabela")

    def setItem(self, row, column, text):
        if row >= self.table.rowCount():
            self.table.insertRow(row)
        self.table.setItem(row, column, QtWidgets.QTableWidgetItem(text, parent=None))

    def create_tab_widget(self):
        self.tab_widget = QtWidgets.QTabWidget(self)
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.delete_tab)
        self.show_tabs()

    def delete_tab(self, index):
        self.tab_widget.removeTab(index)

    
    def open(self):
        self.tab_widget1.setWindowTitle("neki naslov")
    
    def read(self, text):
        putanjaPocinje = text.find("podaci:")
        putanja = text[putanjaPocinje+7:len(text)]
        text = text[0:putanjaPocinje]
        lista = text.split(",")
        counter = 0
        for deo in lista:
            self.setHorizontalHeaderItem(counter, deo)
            counter += 1

        with open(putanja) as f:
            counter = 0
            while True:
                podaci = f.readline()
                print("podaci: ",podaci)
                if podaci == "":
                    break
                listaPodataka = podaci.split(",")
                for i in range(len(lista)):
                    self.setItem(counter, i, listaPodataka[i])
                counter += 1

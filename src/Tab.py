from PySide2 import QtWidgets, QtGui
from PySide2 import QtWidgets
from PySide2.QtWidgets import QAbstractItemView
from klase.student_model import StudentModel
from klase.Student import Student
from PySide2.QtWidgets import QWidget
from PySide2 import QtGui
from klase.polozeni_predmet import PolozeniPredmet
from klase.nepolozeni_predmet import NepolozeniPredmet
from klase.student_model import StudentModel
from klase.polozeni_predmeti_model import PolozeniPredmetiModel
from klase.nepolozeni_predmeti_model import NepolozeniPredmetiModel

class Tab(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.main_layout = QtWidgets.QVBoxLayout()
        self.tab_widget = None
        self.create_tab_widget()
        self.table = QtWidgets.QTableView(self.tab_widget)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.sub_layout = QtWidgets.QHBoxLayout()

        self.btn_up = QtWidgets.QPushButton("↑", self)
        self.btn_down = QtWidgets.QPushButton("<", self)
        self.btn_left = QtWidgets.QPushButton(">", self)
        self.btn_right = QtWidgets.QPushButton("↓", self)

        self.btn_up.setFixedSize(50,80)
        self.btn_down.setFixedSize(50,80)
        self.btn_left.setFixedSize(50,80)
        self.btn_right.setFixedSize(50,80)
        
        self.sub_layout.addStretch()
        
        self.sub_layout.addWidget(self.btn_up)
        self.sub_layout.addWidget(self.btn_down)
        self.sub_layout.addWidget(self.btn_left)
        self.sub_layout.addWidget(self.btn_right)
        self.sub_layout.addStretch()
        self.sub_layout.setSpacing(0)

        self.table.clicked.connect(self.student_selected)
        self.main_layout.addWidget(self.table)
        self.main_layout.addLayout(self.sub_layout)
        self.main_layout.addWidget(self.tab_widget)
        self.setLayout(self.main_layout)

    def show_tabs(self):
        self.tab_widget.addTab(QtWidgets.QTableWidget(1, 1, self.tab_widget), QtGui.QIcon("icons8-edit-file-64.png"), "Prva Podtabela")
        self.tab_widget.addTab(QtWidgets.QTableWidget(1, 1, self.tab_widget), QtGui.QIcon("icons8-edit-file-64.png"), "Druga Podtabela")
    
        
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
        putanja_pocinje = text.find("podaci:")
        putanja = text[putanja_pocinje+7:len(text)]
        text = text[0:putanja_pocinje]
        lista = text.split(",")
        counter = 0
        # for i in range(1, len(lista)):
        #     self.setHorizontalHeaderItem(counter, lista[i])
        #     counter += 1
        pocetak = putanja.rfind("\\")+1
        kraj = putanja.rfind(".")
        
        if putanja[pocetak:kraj] == "studenti":
            student_model = StudentModel()
            with open(putanja) as f:
                counter = 0
                while True:
                    podaci = f.readline()
                    if podaci == "":
                        break
                    listaPodataka = podaci.split(",")
                    student_model.students.append(Student(listaPodataka[0], listaPodataka[1], listaPodataka[2], listaPodataka[3], listaPodataka[4]))
                    counter += 1
                    
            self.table.setModel(student_model)
            # self.set_vertical_header(len(student_model.students))
                
    
    def student_selected(self, index):
        model = self.table.model()
        selected_student = model.get_element(index)
        self.sub_table1 = QtWidgets.QTableView(self.tab_widget)
        self.polozeni_predmeti = PolozeniPredmetiModel()
        for predmet in selected_student.polozeni_predmeti:
            self.polozeni_predmeti.polozeni_predmeti.append(predmet)
        
        self.tab_widget.clear()
        self.sub_table1.setModel(self.polozeni_predmeti)
        self.tab_widget.addTab(self.sub_table1, QtGui.QIcon("icons8-edit-file-64.png"), "Polozeni predmeti")

        self.sub_table2 = QtWidgets.QTableView(self.tab_widget)
        self.nepolozeni_predmeti = NepolozeniPredmetiModel()
        for predmet in selected_student.nepolozeni_predmeti:
            self.nepolozeni_predmeti.nepolozeni_predmeti.append(predmet)
        
        self.sub_table2.setModel(self.nepolozeni_predmeti)
        self.tab_widget.addTab(self.sub_table2, QtGui.QIcon("icons8-edit-file-64.png"), "Nepolozeni predmeti")


        
    # def create_tab_widget(self):
    #     self.tab_widget = QtWidgets.QTabWidget(self)
    #     self.tab_widget.setTabsClosable(True)
    #     self.tab_widget.tabCloseRequested.connect(self.delete_tab)

    # def delete_tab(self, index):
    #     self.tab_widget.removeTab(index)
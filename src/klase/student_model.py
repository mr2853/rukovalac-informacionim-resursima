from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtGui import Qt


class StudentModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.students = [] # nije dvodimenzionalni niz

    # pomocna metoda
    def get_element(self, index):
        return self.students[index.row()]

    def rowCount(self, index):
        return len(self.students)

    def columnCount(self, index):
        return 3

    def data(self, index, role=QtCore.Qt.DisplayRole):
        # TODO: dodati obradu uloga (role)
        student = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return student.index
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return student.ime
        elif index.column() == 2 and role == QtCore.Qt.DisplayRole:
            return student.prezime
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Broj indeksa"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ime"
        elif section == 2 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Prezime"
        elif orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return section+1
        return None

    # metode za editable model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        student = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            student.index = value
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            student.ime = value
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            student.prezime = value
            return True
        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable # ili nad bitovima

    
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtGui import Qt


class Model(QtCore.QAbstractTableModel):
    def __init__(self, nazivi_atributa, nazivi_kolona, parent=None):
        super().__init__(parent)
        self.lista = [] # nije dvodimenzionalni niz
        self.nazivi_atributa = nazivi_atributa
        self.nazivi_kolona = nazivi_kolona
        self.broj_kolona = len(self.nazivi_kolona)

    # pomocna metoda
    def get_element(self, index):
        return self.lista[index.row()]

    def rowCount(self, index):
        return len(self.lista)

    def columnCount(self, index):
        return self.broj_kolona

    def data(self, index, role=QtCore.Qt.DisplayRole):
        # TODO: dodati obradu uloga (role)
        element = self.get_element(index)
        for i in range(self.broj_kolona):
            if i == index.column() and role == QtCore.Qt.DisplayRole:
                return element.__getattribute__(self.nazivi_atributa[i])
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        for i in range(self.broj_kolona):
            if i == section and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.nazivi_kolona[i]

        if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return section+1

        return None

    # metode za editable model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        element = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            element.index = value
            return True
        element = self.get_element(index)
        if value == "":
            return False
        for i in range(self.broj_kolona):
            if index.column() == i and role == QtCore.Qt.EditRole:
                element.__setattr__(self.nazivi_atributa[i], value)
                return True
        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable # ili nad bitovima

    
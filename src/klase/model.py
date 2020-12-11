from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtGui import Qt
import operator
from PySide2.QtCore import Signal


class Model(QtCore.QAbstractTableModel, QtCore.QObject):
    upisan_podatak = QtCore.Signal(int)
    def __init__(self, lista, parent=None):
        super().__init__(parent)
        # self.upisan_podatak
        self.lista_prikaz = []
        self.nazivi_atributa = lista[5].split(",")
        self.nazivi_kolona = lista[10].split(",")
        self.nazivi_kol_atributa = lista[11].split(",")
        self.broj_kolona = len(self.nazivi_kolona)

    # pomocna metoda
    def get_element(self, index):
        return self.lista_prikaz[index.row()]

    def rowCount(self, index):
        return len(self.lista_prikaz)

    def columnCount(self, index):
        return self.broj_kolona

    def data(self, index, role=QtCore.Qt.DisplayRole):
        # TODO: dodati obradu uloga (role)
        element = self.get_element(index)
        for i in range(self.broj_kolona):
            if i == index.column() and role == QtCore.Qt.DisplayRole:
                return element.__getattribute__(self.nazivi_kol_atributa[i])
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        for i in range(self.broj_kolona):
            if i == section and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self.nazivi_kolona[i]

        if orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
            return section+1

        return None

    # metoda za promenu podataka elementa kada se double klik na celiju, menja podatke u listi
    # def setData(self, index, value, role=QtCore.Qt.EditRole):
    #     element = self.get_element(index)
    #     if value == "":
    #         return False
    #     for i in range(self.broj_kolona):
    #         if index.column() == i and role == QtCore.Qt.EditRole:
    #             element.__setattr__(self.nazivi_atributa[i], value)
    #             self.upisan_podatak.emit(0)
    #             return True
    #     return False

    # def flags(self, index):
    #     return super().flags(index) | QtCore.Qt.ItemIsEditable # ili nad bitovima

    def sort_list(self, index, bool_nacin_sortiranja):
        """
        sortira listu
        :param: index - oznacava po kojoj koloni/atributu se sortira
        :param: bool_nacin_sortiranja - oznacava da li je sortiranje prema vecem ili prema manjem elementu
        """
        self.lista_prikaz.sort(key = lambda x: x.__getattribute__(self.nazivi_kol_atributa[index]) , reverse=bool_nacin_sortiranja)
    
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtGui import Qt
import operator
from PySide2.QtCore import Signal

from klase.merge_sort import merge_sort


class Model(QtCore.QAbstractTableModel, QtCore.QObject): #genericki model koji sadrzi sve objekte koje kreiramo
    def __init__(self, lista1, lista2=[], parent=None):
        super().__init__(parent)
        self.lista_prikaz = []
        self.nazivi_atributa = lista1
        if len(lista2) != 0:
            self.nazivi_kolona = lista2
        else:
            self.nazivi_kolona = lista1

        self.broj_kolona = len(self.nazivi_kolona)
        
    # pomocna metoda
    def get_element(self, index):
        return self.lista_prikaz[index.row()]

    def rowCount(self, index):
        return len(self.lista_prikaz)

    def columnCount(self, index):
        return self.broj_kolona
        
    #  #Each item in the model has a set of data elements associated with it, each with its own role. The roles are used by the view to indicate to the model which type of data it needs. Custom models should return data in these types. DisplayRole The key data to be rendered in the form of text.
    def data(self, index, role=QtCore.Qt.DisplayRole): #dobavljanje elemenata
        # TODO: dodati obradu uloga (role)
        element = self.get_element(index)
        for i in range(self.broj_kolona):
            if i == index.column() and role == QtCore.Qt.DisplayRole:
                return element.__getattribute__(self.nazivi_atributa[i])
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole): #prikazivanje hedera tipa ime prezime itd
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
    #             return True
    #     return False

    # def flags(self, index):
    #     return super().flags(index) | QtCore.Qt.ItemIsEditable # ili nad bitovima

    def sort_list(self, index, bool_nacin_sortiranja): #ova metoda se zove u tabu da se sortiraju podaci ukoliko je datoteka sekvencijalna
        """
        sortira listu
        :param: index - oznacava po kojoj koloni/atributu se sortira
        :param: bool_nacin_sortiranja - oznacava da li je sortiranje prema vecem ili prema manjem elementu
        """
        
        self.lista_prikaz = merge_sort(self.lista_prikaz, self.nazivi_atributa[index], bool_nacin_sortiranja)
        
        # self.lista_prikaz.sort(key = lambda x: x.__getattribute__(self.nazivi_atributa[index]) , reverse=bool_nacin_sortiranja)
    
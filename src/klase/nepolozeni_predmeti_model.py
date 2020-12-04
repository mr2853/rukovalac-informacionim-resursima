from PySide2 import QtCore

class NepolozeniPredmetiModel(QtCore.QAbstractTableModel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.nepolozeni_predmeti = [] # nije dvodimenzionalni niz

    # pomocna metoda
    def get_element(self, index):
        return self.nepolozeni_predmeti[index.row()]

    def rowCount(self, index):
        return len(self.nepolozeni_predmeti)

    def columnCount(self, index):
        return 2

    def data(self, index, role=QtCore.Qt.DisplayRole):
        # TODO: dodati obradu uloga (role)
        polozeni_predmet = self.get_element(index)
        if index.column() == 0 and role == QtCore.Qt.DisplayRole:
            return polozeni_predmet.naziv
        elif index.column() == 1 and role == QtCore.Qt.DisplayRole:
            return polozeni_predmet.broj_polaganja
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if section == 0 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Naziv"
        elif section == 1 and orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return "Ocena"
        return None

    # metode za editable model
    def setData(self, index, value, role=QtCore.Qt.EditRole):
        polozeni_predmet = self.get_element(index)
        if value == "":
            return False
        if index.column() == 0 and role == QtCore.Qt.EditRole:
            polozeni_predmet.naziv = value
            return True
        elif index.column() == 1 and role == QtCore.Qt.EditRole:
            polozeni_predmet.broj_polaganja = value
            return True
        return False

    def flags(self, index):
        return super().flags(index) | QtCore.Qt.ItemIsEditable # ili nad bitovima

    
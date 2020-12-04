from .polozeni_predmet import PolozeniPredmet
from .nepolozeni_predmet import NepolozeniPredmet

class Student:
    def __init__(self, index, ime, prezime, polozeni, nepolozeni):
        self.index = index
        self.ime = ime
        self.prezime = prezime
        self.polozeni_predmeti = [PolozeniPredmet(polozeni)]
        self.nepolozeni_predmeti = [NepolozeniPredmet(nepolozeni)]
class Student:
    def __init__(self, ustanova,struka,broj_indeksa,prezime,ime_roditelja,ime,pol,adresa_stanovanja,telefon,JMBG,datum_rodjenja):
        self.ustanova = ustanova
        self.struka = struka
        self.broj_indeksa = broj_indeksa
        self.prezime = prezime
        self.ime_roditelja = ime_roditelja
        self.ime = ime
        self.pol = pol
        self.adresa_stanovanja = adresa_stanovanja
        self.telefon = telefon
        self.JMBG = JMBG
        self.datum_rodjenja = datum_rodjenja

    def __init__(self, lista):
        self.ustanova = lista[0]
        self.struka = lista[1]
        self.broj_indeksa = lista[2]
        self.prezime = lista[3]
        self.ime_roditelja = lista[4]
        self.ime = lista[5]
        self.pol = lista[6]
        self.adresa_stanovanja = lista[7]
        self.telefon = lista[8]
        self.JMBG = lista[9]
        self.datum_rodjenja = lista[10]
    
    def __setitem__(self, i, value):
        if i == 0:
            self.index = value
        elif i == 1:
            self.ime = value
        elif i == 2:
            self.prezime = value
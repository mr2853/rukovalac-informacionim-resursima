class Student:
    def __init__(self,*args): # *args pokazuje na niz parametara koji je prosledjen
        """
        ustanova | struka | broj_indeksa | prezime | ime_roditelja | ime | pol | adresa_stanovanja | telefon | JMBG | datum_rodjenja
        """
        if len(args) == 11: # ako je niz duzine 10 znaci ima 10 parametara 
            self.constructor1(args)
        elif len(args) == 1: # ako je duzine 1 znaci ima 1 parametar
            self.constructor2(args)
            
    def constructor1(self, *args): # i ovde svaki parametar redom dodeljuje gde je potrebno
        self.ustanova = args[0]
        self.struka = args[1]
        self.broj_indeksa = args[2]
        self.prezime = args[3]
        self.ime_roditelja = args[4]
        self.ime = args[5]
        self.pol = args[6]
        self.adresa_stanovanja = args[7]
        self.telefon = args[8]
        self.JMBG = args[9]
        self.datum_rodjenja = args[10]
        return self
        
    def constructor2(self, *args): # ovde ima samo 1 parametar, taj parametar je lista
        lista = [] 
        lista = args[0][0] # ovde iz niza args uzimamo prvi element i onda mora opet [0] da bi prosledilo samo listu bez dodatnih ()
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
        return self
    

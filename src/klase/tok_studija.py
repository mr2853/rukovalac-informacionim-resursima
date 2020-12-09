class TokStudija:
    def __init__(self, *args):
       
        if len(args) == 13:
            self.constructor1(args)
        elif len(args) == 1:
            self.constructor2(args)
       
    def constructor1(self, *args):
        self.ustanova = args[0]
        self.oznaka_programa = args[1]
        self.student_iz_ustanove = args[2]
        self.struka = args[3]
        self.broj_indeksa = args[4]
        self.skolska_godina = args[5]
        self.godina_studija = args[6]
        self.blok = args[7]
        self.redni_broj_upisa = args[8]
        self.datum_upisa = args[9]
        self.datum_overe = args[10]
        self.espb_pocetni = args[11]
        self.espb_krajnji = args[12]
        return self

    def constructor2(self, *args):
        lista = []
        lista = args[0][0]
        self.ustanova = lista[0]
        self.oznaka_programa = lista[1]
        self.student_iz_ustanove = lista[2]
        self.struka = lista[3]
        self.broj_indeksa = lista[4]
        self.skolska_godina = lista[5]
        self.godina_studija = lista[6]
        self.blok = lista[7]
        self.redni_broj_upisa = lista[8]
        self.datum_upisa = lista[9]
        self.datum_overe = lista[10]
        self.espb_pocetni = lista[11]
        self.espb_krajnji = lista[12]
        return self

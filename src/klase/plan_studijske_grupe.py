class Plan_studijske_Grupe:
    def __init__(self,*args):
        
        if len(args) == 6:
            self.constructor1(args)
        elif len(args) == 1:
            self.constructor2(args)
        

    def constructor1(self, *args):   
        self.program_ustanove = args[0]
        self.oznaka_programa = args[1]
        self.blok = args[2]
        self.pozicija = args[3]
        self.ustanova_predmet = args[4]
        self.oznaka_predmeta = args[5]
        return self

    def constructor2(self, *args):
        lista = []
        lista = args[0][0]   
        self.program_ustanove = lista[0]
        self.oznaka_programa = args[1]
        self.blok = args[2]
        self.pozicija = args[3]
        self.ustanova_predmet = args[4]
        self.oznaka_predmeta = args[5]
        return self
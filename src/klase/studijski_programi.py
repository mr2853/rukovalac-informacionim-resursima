class Studijski_programi:
    def __init__(self,*args):
        
        
        if len(args) == 4:
            self.constructor1(args)
        elif len(args) == 1:
            self.constructor2(args)

    def constructor1(self, *args):
        self.ustanova = args[0]
        self.nivo = args[1]
        self.oznaka_programa = args[2]
        self.naziv_programa = args[3]
        return self

    def constructor2(self, *args):
        lista = []
        lista = args[0][0]
        self.ustanova = lista[0]
        self.nivo = lista[1]
        self.oznaka_programa = lista[2]
        self.naziv_programa = lista[3]
        return self
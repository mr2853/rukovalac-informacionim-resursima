class Predmet:
    def __init__(self,*args):
        if len(args) == 4:
            self.constructor1(args)
        elif len(args) == 1:
            self.constructor2(args)

        
    def constructor1(self, *args):
        self.ustanova = args[1]
        self.oznaka = args[2]
        self.naziv = args[3]
        self.espb = args[4]
        return self

    def constructor2(self, *args):
        lista = []
        lista = args[0][0]
        self.ustanova = lista[0]
        self.oznaka = lista[1]
        self.naziv = lista[2]
        self.espb = lista[3]
        return self
    

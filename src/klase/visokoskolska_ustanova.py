class VisokoskolskaUstanova:
    def __init__(self, *args):
        if len(args) == 3:
            self.construktor1(args)
        elif len(args) == 1:
            self.construktor2(args)


    def construktor1(self, *args):
        self.oznaka = args[0]
        self.naziv = args[1]
        self.adresa = args[2]
        return self

    def construktor2(self, *args):
        lista = []
        lista = args[0][0]
        self.oznaka = lista[0]
        self.naziv = lista[1]
        self.adresa = lista[2]
        return self
      



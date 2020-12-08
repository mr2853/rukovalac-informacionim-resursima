class Nivo_studija:
    def __init__(self, *args):
        if len(args) == 2:
            self.constructor1(args)
        elif len(args) == 1: 
            self.constructor2(args)
        
        
    def constructor1(self, *args):    
        self.oznaka = args[0]
        self.naziv = args[1]
        return self

    def constructor2(self, *args):
        
        lista = [] 
        lista = args[0][0]
        self.oznaka = lista[0]
        self.naziv = lista[1]
        return self

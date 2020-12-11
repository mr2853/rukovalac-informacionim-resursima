

class GenerickaKlasa:
    def __init__(self, *args):
        
        if len(args) > 0:
            self.constructor1(args)
        elif type(args) == list:
            self.constructor2(args)


                
    def constructor1(self, *args):    
        i=0
        for i in range(len(args)-1):
            
            self.atribut = args[i]
        
        return self
            

    def constructor2(self, *args):
        
        lista = [] 
        lista = args[0][0]
        i=0
        for i in args:
            self.atribut = lista[i]
     
        
        return self

    


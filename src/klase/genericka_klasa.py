class GenerickaKlasa:
    def __init__(self, lista_atributa, lista_podataka):
        for i in range(len(lista_atributa)):
            self.__setattr__(lista_atributa[i], lista_podataka[i])
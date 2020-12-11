import csv
from types import new_class
from .model import Model
from .genericka_klasa import GenerickaKlasa

def citanje_meta_podataka(putanja):
    neka_lista = []
    with open(putanja, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = "\n")
        counter = 0
        for row in spamreader:
            dve_tacke = row[0].find(":")+1
            row[0] = row[0][dve_tacke:len(row[0])]

            if counter == 4:
                del1 = row[0].find("\\")
                del2 = row[0].find(".") + 1
                row[0] = row[0][del1:del2]
                row[0] = neka_lista[2] + row[0] + neka_lista[3]
                
            neka_lista.append(row[0])
            counter += 1
            
    return neka_lista

def kreiraj_model(lista):
    model = Model(lista)
    with open(lista[4], newline='\n') as f:
        while True:
            podaci = f.readline().strip()
            if podaci == "":
                break
            
            lista_podataka = podaci.split(",")
            model.lista_prikaz.append(GenerickaKlasa(lista[5].split(","), lista_podataka))

    return model
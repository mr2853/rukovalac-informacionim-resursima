import csv
from .model import Model
from .genericka_klasa import GenerickaKlasa

def citanje_meta_podataka(putanja, bez_putanje=False): 
    neka_lista = []
    with open(putanja, 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = "\n")
        counter = 0
        for row in spamreader:
            if row[0] == "":
                continue
            dve_tacke = row[0].find(":")+1
            row[0] = row[0][dve_tacke:len(row[0])]

            if counter == 4 and not bez_putanje:
                del1 = row[0].find("\\")
                del2 = row[0].find(".") + 1
                row[0] = row[0][del1:del2]
                row[0] = neka_lista[2] + row[0] + neka_lista[3]
                
            neka_lista.append(row[0])
            counter += 1
            
    return neka_lista

def kreiraj_model(meta_podaci, tab=None, naziv=""):
    if meta_podaci[1] != "sql":
        model = Model(meta_podaci[5].split(","), meta_podaci[10].split(","), meta_podaci[11].split(","))
        prva_linija = True
        with open(meta_podaci[4], 'r', newline='\n') as f:
            while True:
                podaci = f.readline().strip()
                if prva_linija:
                    prva_linija = False
                    continue

                if podaci == "":
                    break
                
                lista_podataka = podaci.split(",")
                model.lista_prikaz.append(GenerickaKlasa(meta_podaci[5].split(","), lista_podataka))
    else:
        parent = tab.pocetna_strana
            
        model = Model(meta_podaci[5].split(","), meta_podaci[10].split(","), meta_podaci[11].split(","))
        query = "SELECT * FROM " + naziv
        parent.csor.execute(query)

        for result in parent.csor.fetchall():
            lista_podataka = []
            for i in result:
                lista_podataka.append(str(i))
                
            model.lista_prikaz.append(GenerickaKlasa(meta_podaci[5].split(","), lista_podataka))

    return model

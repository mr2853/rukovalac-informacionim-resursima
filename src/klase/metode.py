import csv
from types import new_class

from PySide2.QtCore import QModelIndex
from .model import Model
from .genericka_klasa import GenerickaKlasa
from .merge_sort import merge_sort
from PySide2 import QtWidgets
import os

def citanje_meta_podataka(putanja):
    neka_lista = []
    with open(putanja, 'r', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = "\n")
        counter = 0
        for row in spamreader:
            if row[0] == "":
                continue
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
    prva_linija = True
    with open(lista[4], 'r', newline='\n') as f:
        while True:
            podaci = f.readline().strip()
            if prva_linija:
                prva_linija = False
                continue

            if podaci == "":
                break
            
            lista_podataka = podaci.split(",")
            model.lista_prikaz.append(GenerickaKlasa(lista[5].split(","), lista_podataka))

    return model

def pretraga(lista_kljuceva, lista_kriterijuma, lista_vece_manje, meta_podaci):
    model = Model(meta_podaci)
    with open(meta_podaci[4], 'r', newline='\n') as f:
        prva_linija = True
        while True:
            podaci = f.readline().strip()
            if prva_linija:
                prva_linija = False
                continue
            if podaci == "":
                break
            
            lista_podataka = podaci.split(",")
            lista_atributa = meta_podaci[5].split(",")
            for i in range(len(lista_podataka)):
                proslo = False
                for j in range(len(lista_kljuceva)):
                    if lista_atributa[i] == lista_kljuceva[j]:
                        if lista_vece_manje[j] == 0:
                            if lista_podataka[i] < lista_kriterijuma[j]:
                                proslo = True
                        elif lista_vece_manje[j] == 1:
                            if lista_podataka[i] <= lista_kriterijuma[j]:
                                proslo = True
                        elif lista_vece_manje[j] == 2:
                            if lista_podataka[i] > lista_kriterijuma[j]:
                                proslo = True
                        elif lista_vece_manje[j] == 3:
                            if lista_podataka[i] >= lista_kriterijuma[j]:
                                proslo = True
                        elif lista_vece_manje[j] == 4:
                            if lista_podataka[i] == lista_kriterijuma[j]:
                                proslo = True
                if proslo:
                    model.lista_prikaz.append(GenerickaKlasa(lista_atributa, lista_podataka))

    return model

def spoji_dve_sekvencijalne_datoteke(putanja_privremena, putanja_originalna, kljuc, nacin_sortiranja, nova_putanja=""):
    """
    :param putanja_privremena: putanja prve datoteke
    :param putanja_originalna: putanja druge datoteke
    :param kljuc: kljuc po kom se sortira kljuc = ["indeks_kljuca"-int, "vrednost_kljuca"-string]
    :param nacin_sortiranja: True/False da li je u rastucem redosledu ili opadajucem

    """
    if nova_putanja == "":
        nova_putanja = putanja_originalna

    lista_ser = []
    prva_meta = ""
    prva_linija = True
    with open(putanja_privremena, 'r', newline='') as f:
        reader = csv.reader(f, delimiter = ",")
        for row in reader:
            if len(row) == 0:
                break
            if prva_linija:
                prva_meta = row
                prva_linija = False
                continue
            lista_ser.append(row)

    lista_sek = []
    prva_linija = True
    iste = True
    with open(putanja_originalna, 'r', newline='') as f:
        reader = csv.reader(f, delimiter = ",")
        for row in reader:
            if len(row) == 0:
                break
            if prva_linija:
                prva_linija = False
                if row != prva_meta:
                    iste = False
                    break
                continue
            lista_sek.append(row)
    if not iste:
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Datoteke koje ste izabrali ne sadrze isti tip informacija")
        msgBox.exec()
        return

    for i in lista_ser:
        lista_sek.append(i)

    merge_sort(lista_sek, kljuc[0], nacin_sortiranja) # za svaki slucaj i sortiramo

    with open(nova_putanja, 'a', newline='') as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow(prva_meta)
        for i in range(len(lista_sek)):
            writer.writerow(lista_sek[i])
        
def sastavi_sekvencijalnu(parent):
    lista_atributa = parent.lista_atributa
    lista_kljuceva = parent.lista_kljuceva
    putanja_serijske = parent.privremena_datoteka
    putanja_sekvencijalne = parent.putanja_podaci
    nacin_sortiranja = True
    broj_novih_objekata = 0

    lista_objekata = []
    with open(putanja_serijske, 'r', newline='\n') as f:
        prva_linija = True
        while True:
            podaci = f.readline().strip()
            if prva_linija:
                prva_linija = False
                continue
            if podaci == "":
                break
            
            lista_podataka = podaci.split(",")
            lista_objekata.append(GenerickaKlasa(lista_atributa, lista_podataka))
            broj_novih_objekata += 1

    with open(putanja_sekvencijalne, 'r', newline='\n') as f:
        prva_linija = True
        while True:
            podaci = f.readline().strip()
            if prva_linija:
                prva_linija = False
                continue
            if podaci == "":
                break
            
            lista_podataka = podaci.split(",")
            lista_objekata.append(GenerickaKlasa(lista_atributa, lista_podataka))

    lista_istih = []
    for j in range(len(lista_objekata)-1):
        for m in range(j+1, len(lista_objekata)):
            nadjen = False
            for i in range(len(lista_kljuceva)):
                if lista_objekata[j].__getattribute__(lista_kljuceva[i]) == lista_objekata[m].__getattribute__(lista_kljuceva[i]):
                    nadjen = True
            if nadjen:
                for n in range(len(lista_istih)):
                    for z in range(len(lista_istih[n])):
                        if lista_istih[n][z] == j:
                            sadrzi = False
                            for s in range(z+1, len(lista_istih[n])):
                                if lista_istih[n][s] == m:
                                    sadrzi = True
                                    break
                            if sadrzi:
                                nadjen = False
                                continue
                            
                            lista_istih[n].append(m)
                            nadjen = False
                            break
                    if not nadjen:
                        break
                if nadjen:
                    lista_istih.append([j,m])

    while len(lista_istih) != 0:
        list_tuple = () # ponavljati ovo koliko ima elementa sa duplikatima
        for i in range(len(lista_istih[0])):
            tekst = ""
            for j in range(len(lista_atributa)):
                tekst += str(lista_objekata[lista_istih[0][i]].__getattribute__(lista_atributa[j]))
                if j < len(lista_atributa)-1:
                    tekst += ","

            list_tuple = list_tuple + (tekst,)

        input = QtWidgets.QInputDialog.getItem(
            parent, 
            "",
            "Uneli ste vise elemenata sa nekim istim podacima koji moraju biti jedinstveni\n"
            "Izaberite koji element zelite da zadrzite:",
            list_tuple,
            0,
            editable=False)
            
        if input[1]:
            for i in range(len(list_tuple)):
                if list_tuple[i].find(input[0]) != -1:
                    lista_istih[0].pop(i)
                    break
            
            for i in range(len(lista_istih[0])):
                lista_objekata.pop(lista_istih[0][i])
                for j in range(len(lista_istih)):
                    for m in range(len(lista_istih[j])):
                        if lista_istih[0][i] <= lista_istih[j][m]:
                            lista_istih[j][m] -= 1

                broj_novih_objekata -= 1
                
            lista_istih.pop(0)
        else:
            return False
            
    merge_sort(lista_objekata, lista_kljuceva[0], nacin_sortiranja)
    
    model = parent.parent().table.model()
    model.lista_prikaz = []
    parent.parent().table
    with open(putanja_sekvencijalne, 'w', newline='') as f:
        writer = csv.writer(f, delimiter = ",")
        writer.writerow([parent.parent().putanja_meta])
        for i in range(len(lista_objekata)):
            tekst = ""
            model.lista_prikaz.append(lista_objekata[i])
            for j in range(len(lista_atributa)):
                tekst += str(lista_objekata[i].__getattribute__(lista_atributa[j]))
                if j < len(lista_atributa)-1:
                    tekst += ","
            novi_red = tekst.split(",")
            writer.writerow(novi_red)

    parent.parent().table.model().beginInsertRows(QModelIndex(), 0, broj_novih_objekata - 1)
    parent.parent().table.setModel(model)
    parent.parent().table.model().endInsertRows()
    return True

def dodaj_u_serijsku(objekat, lista_atributa, putanja, meta_putanja):
    postoji = True
    relativna_putanja = ""
    if not os.path.exists(putanja):
        postoji = False
        trenutni_direk = os.getcwd()
        relativna_putanja = os.path.relpath(meta_putanja, trenutni_direk)

    with open(putanja, 'a', newline='',encoding="utf-8") as f:
        writer = csv.writer(f, delimiter = ",")
        if postoji == False:
            writer.writerow([relativna_putanja])

        tekst = ""
        for j in range(len(lista_atributa)):
            tekst += str(objekat.__getattribute__(lista_atributa[j]))
            if j < len(lista_atributa)-1:
                tekst += ","
                
        novi_red = tekst.split(",")
        writer.writerow(novi_red)
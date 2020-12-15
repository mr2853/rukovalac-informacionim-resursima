import csv
from types import new_class
from .model import Model
from .genericka_klasa import GenerickaKlasa
from .merge_sort import merge_sort
from PySide2 import QtWidgets

def citanje_meta_podataka(putanja):
    neka_lista = []
    with open(putanja, newline='') as csvfile:
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
    with open(lista[4], newline='\n') as f:
        while True:
            podaci = f.readline().strip()
            if podaci == "":
                break
            
            lista_podataka = podaci.split(",")
            model.lista_prikaz.append(GenerickaKlasa(lista[5].split(","), lista_podataka))

    return model

def pretraga_serijske(lista_kljuceva, lista_kriterijuma, meta_podaci):
    model = Model(meta_podaci)
    with open(meta_podaci[4], newline='\n') as f:
        while True:
            podaci = f.readline().strip()
            if podaci == "":
                break
            
            lista_podataka = podaci.split(",")
            lista_atributa = meta_podaci[5].split(",")
            for i in range(len(lista_podataka)):
                proslo = False
                for j in range(len(lista_kljuceva)):
                    if lista_atributa[i] == lista_kljuceva[j]:
                        if lista_podataka[i] == lista_kriterijuma[j]:
                            proslo = True
                if proslo:
                    model.lista_prikaz.append(GenerickaKlasa(lista_atributa, lista_podataka))

    return model

# prototip funkcije kako ce odprilike izgledati
# implementirati kada to bude moguce i testirati
def spoji_dve_sekvencijalne_datoteke(putanja_privremena, putanja_originalna, index_prvog_kljuca, nacin_sortiranja):
    lista_ser = []
    with open(putanja_privremena, 'r', newline='') as f:
        reader = csv.reader(f, delimiter = ",")
        for row in reader:
            if row[0] == "":
                break
            lista_ser.append(row[0].split(","))

    lista_sek = []
    with open(putanja_originalna, 'r', newline='') as f:
        reader = csv.reader(f, delimiter = ",")
        nadjen = False
        for row in reader:
            if row[0] == "":
                break
            deo = row[0].split(",")
            if nacin_sortiranja:
                if deo[index_prvog_kljuca] > lista_ser[0][index_prvog_kljuca] or nadjen:
                    lista_sek.append(deo)
                    nadjen = True
            else:
                if deo[index_prvog_kljuca] < lista_ser[0][index_prvog_kljuca] or nadjen:
                    lista_sek.append(deo)
                    nadjen = True
    
    for i in lista_ser:
        lista_sek.append(i)
    
    # ovde umesto index_prvog_kljuca treba proslediti string naziv kljuca
    merge_sort(lista_sek, index_prvog_kljuca, nacin_sortiranja)

    with open(putanja_originalna, 'w', newline='') as f:
        writer = csv.writer(f, delimiter = ",")
        for i in range(len(lista_sek)):
            writer.writerow([lista_sek[i]])
        

# prototip funkcije kako ce odprilike izgledati
# implementirati kada to bude moguce i testirati
def dodavanje_u_sekvencijalnu(lista_atributa, lista_kljuceva, putanja_serijske, putanja_sekvencijalne, nacin_sortiranja):
    lista_objekata = []
    with open(putanja_serijske, newline='\n') as f: # mozda se ovaj pocetak moze bolje resiti da uporedo otvorim
        while True:                            # dve datoteke pa da proveram da li je kljuc jednak, ali opet onda
            podaci = f.readline().strip()   # treba videti kako korisniku ponuditi da izabere kojeg da sacuva...
            if podaci == "":
                break
            
            lista_podataka = podaci.split(",")
            lista_objekata.append(GenerickaKlasa(lista_atributa, lista_podataka))

    with open(putanja_sekvencijalne, newline='\n') as f:
        while True:
            podaci = f.readline().strip()
            if podaci == "":
                break
            
            lista_podataka = podaci.split(",")
            lista_objekata.append(GenerickaKlasa(lista_atributa, lista_podataka))

    lista_istih = []
    for i in range(len(lista_kljuceva)):
        for j in range(len(lista_objekata)):
            for m in range(j, len(lista_objekata)):
                if lista_objekata[j].__getattribute__(lista_kljuceva[i]) == lista_objekata[m].__getattribute__(lista_kljuceva[i]):
                    nadjen = False
                    for n in range(len(lista_istih)):
                        if lista_istih[n][0] == j:
                            lista_istih[n].append(m)
                            nadjen = True
                            break
                    if not nadjen:
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
            QtWidgets.QWidget, # staviti self umesto QtWidgets.QWidget ili videti sta proslediti ovde 
            "",
            "Uneli ste vise elemenata sa nekim istim podacima koji moraju biti jedinstveni\n"
            "Izaberite koji element zelite da zadrzite:",
            list_tuple,
            0,
            editable=False)
            
        if input[1]:
            index = -1
            for i in range(list_tuple):
                if list_tuple[i].find(input[0]) != -1:
                    index = i
                    break
            
            if index == -1:
                ... # pogresan unos poruka
                # nekako je izabrana nepostojeci element
                # obavestiti korisnika i vratiti ga

            for i in range(len(lista_istih[0])):
                if index != i:
                    lista_objekata.remove(lista_objekata[lista_istih[0][i]])

            lista_istih.remove(lista_istih[0])
        else:
            ... # poruka da li zeli sigurno da prekine
            # ako da, prekinuti while petlju
            # ako ne, samo ga vratiti u petlju

    merge_sort(lista_objekata, lista_kljuceva[0], True) # proveriti da li da bude po prvom kljucu
                                                # i sortiranje da li treba da bude Ascending ili Descending
    
    with open(putanja_serijske, 'w', newline='') as f:
        writer = csv.writer(f, delimiter = ",")
        tekst = ""
        for i in range(len(lista_objekata)):
            for j in range(len(lista_atributa)):
                tekst += str(lista_objekata[i].__getattribute__(lista_atributa[j]))
                if j < len(lista_atributa)-1:
                    tekst += ","
            novi_red = tekst.split(",")
            writer.writerow(novi_red)

    index_prvog_kljuca = -1
    for i in range(len(lista_atributa)):
        if lista_atributa[i] == lista_kljuceva[0]:
            index_prvog_kljuca = i

    spoji_dve_sekvencijalne_datoteke(putanja_serijske, 
                    putanja_sekvencijalne,
                    index_prvog_kljuca, nacin_sortiranja)

# prototip funkcije kako ce odprilike izgledati
# implementirati kada to bude moguce i testirati
def dodaj_u_serijsku(objekat, lista_atributa, putanja):
    with open(putanja, 'a', newline='') as f:
        writer = csv.writer(f, delimiter = ",")
        tekst = ""
        for j in range(len(lista_atributa)):
            tekst += str(objekat.__getattribute__(lista_atributa[j]))
            if j < len(lista_atributa)-1:
                tekst += ","
                
        novi_red = tekst.split(",")
        writer.writerow(novi_red)
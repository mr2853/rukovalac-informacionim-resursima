import csv
import os

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
def quick_sort(s, atribut, bool_nacin_sortiranja):
    """
    Metod sortiranja koji koristi rekurziju.
    Na osnovu pivot elementa deli strukturu s u 3 liste:
        l - struktura gde ce se smestiti svi elementi iz s koji su manji od pivot elementa
        e - struktura gde ce se smestiti svi elementi iz s koji su jednaki pivot elementu
        g - struktura gde ce se smestiti svi elementi iz s koji su veci od pivot elementa
    :param s: struktura koju sortiramo
    :return:
    """
    if bool_nacin_sortiranja:
        n = len(s)  # dobavljamo podatak o duzini strukture
        if n < 2: # ako lista ima 1 element ona je vec sortirana
            return  # lista je vec sortirana
        pivot = s[0].__getattribute__(atribut)  # uzimamo prvi element liste za pivot element
        l = []  # lista koja ce biti popunjena elementima koji su manji od pivota
        e = []  # lista koja ce biti popunjena elementima koji su jednaki pivotu
        g = []  # lista koja ce biti popunjena elementima koji su veci od pivota
        while not (len(s) == 0):  # sve dok lista s nije prazna
            # podeli
            if s[0].__getattribute__(atribut) < pivot:  # provera da li element treba da ide u listu l
                l.append(s.pop(0))  # uklanjamo element iz liste i dodajemo ga u listu l
            elif pivot < s[0].__getattribute__(atribut):  # provera da li element treba da ide u listu g
                g.append(s.pop(0))  # dodavanje u listu g
            else:  # ukoliko nije striktno manji i striktno veci onda je jednak pivot elementu
                e.append(s.pop(0))  # dodavanje uklonjenog elementa u listu e
        # zavladaj
        quick_sort(l, atribut, bool_nacin_sortiranja)  # rekurzivno sortiramo manje liste
        quick_sort(g, atribut, bool_nacin_sortiranja)
        # kombinuj
        while not (len(l) == 0):  # sve dok ne ispraznimo listu elemenata manjih od pivota
            s.append(l.pop(0))  # dodajemo ih redom u pocetnu listu, koja ce biti nas rezultat
        while not (len(e) == 0):  # sve dok ne ispraznimo listu elemenata koji su jednaki pivot elementu
            s.append(e.pop(0))  # dodajemo ih redom u pocetnu listu, u kojoj vec imamo sve elemente manje od pivota
        while not (len(g) == 0):  # sve dok ne ispraznimo listu elemenata koji su veci od pivot elementa
            s.append(g.pop(0))  # dodajemo ih redom u pocetnu listu, u kojoj vec imamo sve elemente koji su i manji i jednaki pivot elementu
    else:
        n = len(s)  # dobavljamo podatak o duzini strukture
        if n < 2: # ako lista ima 1 element ona je vec sortirana
            return  # lista je vec sortirana
        pivot = s[0].__getattribute__(atribut)  # uzimamo prvi element liste za pivot element
        l = []  # lista koja ce biti popunjena elementima koji su manji od pivota
        e = []  # lista koja ce biti popunjena elementima koji su jednaki pivotu
        g = []  # lista koja ce biti popunjena elementima koji su veci od pivota
        while not (len(s) == 0):  # sve dok lista s nije prazna
            # podeli
            if s[0].__getattribute__(atribut) > pivot:  # provera da li element treba da ide u listu l
                l.append(s.pop(0))  # uklanjamo element iz liste i dodajemo ga u listu l
            elif pivot > s[0].__getattribute__(atribut):  # provera da li element treba da ide u listu g
                g.append(s.pop(0))  # dodavanje u listu g
            else:  # ukoliko nije striktno manji i striktno veci onda je jednak pivot elementu
                e.append(s.pop(0))  # dodavanje uklonjenog elementa u listu e
        # zavladaj
        quick_sort(l, atribut, bool_nacin_sortiranja)  # rekurzivno sortiramo manje liste
        quick_sort(g, atribut, bool_nacin_sortiranja)
        # kombinuj
        while not (len(l) == 0):  # sve dok ne ispraznimo listu elemenata manjih od pivota
            s.append(l.pop(0))  # dodajemo ih redom u pocetnu listu, koja ce biti nas rezultat
        while not (len(e) == 0):  # sve dok ne ispraznimo listu elemenata koji su jednaki pivot elementu
            s.append(e.pop(0))  # dodajemo ih redom u pocetnu listu, u kojoj vec imamo sve elemente manje od pivota
        while not (len(g) == 0):  # sve dok ne ispraznimo listu elemenata koji su veci od pivot elementa
            s.append(g.pop(0))  # dodajemo ih redom u pocetnu listu, u kojoj vec imamo sve elemente koji su i manji i jednaki pivot elementu
    
from .quick_sort import quick_sort

def list_split(l):
    i = 1
    lista = []
    while True:
        pocetak = 0
        mid = len(l)//i
        if mid < 100000:
            while i != 0:
                if mid >= len(l):
                    lista.append(l[pocetak:len(l)])
                    return lista
                lista.append(l[pocetak:mid])
                pocetak = mid
                mid += mid
                i -= 1
            return lista
        i += 1

def merge(s1, s, atribut, bool_nacin_sortiranja):
    """
    Spaja sortirane sekvence s1 i s2 u rezultujucu sekvencu s.
    :param s1: sortirana leva polovna liste s
    :param s2: sortirana desna polovina liste s
    :param s: lista koju cemo reorganizovati spram prethodno sortiranih polovina
    :return:
    """
    if bool_nacin_sortiranja:
        i = k = 0  # indeksi za kretanje po sekvencama s1, s2 i s
        j = 1
        # za s1 koristimo i, za s2 koristimo j, i za s koristimo k
        kraj = 0
        while k < len(s1)-1:  # ukoliko nismo prosli bar jednu od listi
            if i == j:
                i += 1
                
            if s1[i].__getattribute__(atribut) < s1[j].__getattribute__(atribut):  # uporedi trenutnim pozicijama listi s1 i s2 koji je manji element
                s[k] = s1[i]  # dodeli manji element u listu s
                i += 1 # inkrementiraj brojac i, kako se dodati broj vise ne bi poredio sa drugim elementima
                kraj = 0
            else:  # ukoliko je veci
                s[k] = s1[j]  # dodeli veci element u listu s
                j += 1  # inkrementiraj brojac j
                kraj = 1
            k += 1  # inkrementiraj brojac k kojim označavamo da smo popunili odgovarajući element liste
        if kraj == 0:
            s[k] = s1[j]
        else:
            s[k] = s1[i]
    else:
        i = k = 0  # indeksi za kretanje po sekvencama s1, s2 i s
        j = 1
        # za s1 koristimo i, za s2 koristimo j, i za s koristimo k
        kraj = 0
        while k < len(s1)-1:  # ukoliko nismo prosli bar jednu od listi
            if i == j:
                i += 1
                
            if s1[i].__getattribute__(atribut) > s1[j].__getattribute__(atribut):  # uporedi trenutnim pozicijama listi s1 i s2 koji je manji element
                s[k] = s1[i]  # dodeli manji element u listu s
                i += 1 # inkrementiraj brojac i, kako se dodati broj vise ne bi poredio sa drugim elementima
                kraj = 0
            else:  # ukoliko je veci
                s[k] = s1[j]  # dodeli veci element u listu s
                j += 1  # inkrementiraj brojac j
                kraj = 1
            k += 1  # inkrementiraj brojac k kojim označavamo da smo popunili odgovarajući element liste
        if kraj == 0:
            s[k] = s1[j]
        else:
            s[k] = s1[i]

def merge_sort(s, atribut, bool_nacin_sortiranja):
    """
    :param s: lista koju je potrebno sortirati
    :param atribut: kljuc po kom da se sortira lista
    :param bool_nacin_sortiranja: True u rastucem redosledu, False u opadajucem
    """
    if len(s) > 1: # ako nije trivijalni problem (jedan element u listi ili 0 elemenata)
        # podeli
        s1 = list_split(s)
        
        # zavladaj
        for i in s1:
            quick_sort(i, atribut, bool_nacin_sortiranja)
            
        # kombinuj
        s2 = []
        for i in s1[0]:
            s2.append(i)
        
        merge(s2, s, atribut, bool_nacin_sortiranja)
        return s
    else:
        return
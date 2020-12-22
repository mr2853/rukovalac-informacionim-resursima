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
    n = len(s)
    
    if n < 2:
        return
        
    if isinstance(atribut, int) != True:
        pivot = s[0].__getattribute__(atribut)
    else:
        pivot = s[0][atribut]  

    l = []  
    e = []  
    g = []  
    
    while not (len(s) == 0):
        if isinstance(atribut, int) != True:
            if s[0].__getattribute__(atribut) > pivot: 
                g.append(s.pop(0)) 
            elif s[0].__getattribute__(atribut) < pivot: 
                l.append(s.pop(0)) 
            else: 
                e.append(s.pop(0))
        else:
            if s[0][atribut] > pivot:
                g.append(s.pop(0)) 
            elif s[0][atribut] < pivot: 
                l.append(s.pop(0)) 
            else:  
                e.append(s.pop(0))

    quick_sort(l, atribut, bool_nacin_sortiranja)  # rekurzivno sortiramo manje liste
    quick_sort(g, atribut, bool_nacin_sortiranja)
    # kombinuj
    
    # print("--------------------------")
    # for i in range(len(l)):
    #     print("l:",l[i].__getattribute__(atribut))
    # for i in range(len(g)):
    #     print("g:",g[i].__getattribute__(atribut))
    # for i in range(len(e)):
    #     print("e:",e[i].__getattribute__(atribut))
    # print("++++++++++++++++++++++++++")
    if bool_nacin_sortiranja:
        while not (len(g) == 0):
            s.append(g.pop(0)) 
        while not (len(e) == 0): 
            s.append(e.pop(0))  
        while not (len(l) == 0): 
            s.append(l.pop(0)) 
    else:
        while not (len(l) == 0):  # sve dok ne ispraznimo listu elemenata manjih od pivota
            s.append(l.pop(0))  # dodajemo ih redom u pocetnu listu, koja ce biti nas rezultat
        while not (len(e) == 0):  # sve dok ne ispraznimo listu elemenata koji su jednaki pivot elementu
            s.append(e.pop(0))  # dodajemo ih redom u pocetnu listu, u kojoj vec imamo sve elemente manje od pivota
        while not (len(g) == 0):  # sve dok ne ispraznimo listu elemenata koji su veci od pivot elementa
            s.append(g.pop(0))  # dodajemo ih redom u pocetnu listu, u kojoj vec imamo sve elemente koji su i manji i jednaki pivot elementu
    
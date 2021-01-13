from .quick_sort import quick_sort

def list_split(l):
    deo = 100
    lista = [l[x:x+deo] for x in range(0, len(l), deo)]
    return lista

def merge(s1, s, atribut, bool_nacin_sortiranja):
    """
    Spaja sortirane sekvence s1 i s2 u rezultujucu sekvencu s.
    :param s1: lista sortiranih listi
    :param s: lista u koju se cuva
    :param s: lista koju cemo reorganizovati spram prethodno sortiranih polovina
    :return:
    """
    if bool_nacin_sortiranja:
        i = k = 0 
        j = 1
        # za s1 koristimo i, za s2 koristimo j, i za s koristimo k
        kraj = 0
        while k < len(s1)-1: 
            if i == j:
                if kraj == 0:
                    s[k] = s1[j]  
                    j += 1 
                else:
                    s[k] = s1[i]  
                    i += 1 
            
            if isinstance(atribut, int) != True:
                prvi = 0
                drugi = 0
                try:
                    prvi = int(s1[i][atribut])
                    drugi = int(s1[j][atribut])
                except ValueError:
                    prvi = s1[i][atribut]
                    drugi = s1[j][atribut]
                except TypeError:
                    prvi = s1[i].__getattribute__(atribut)
                    drugi = s1[j].__getattribute__(atribut)
                    
                if prvi > drugi:  
                    s[k] = s1[i]  
                    i += 1 
                    kraj = 0
                else:  
                    s[k] = s1[j]  
                    j += 1  
                    kraj = 1
            else:
                prvi = 0
                drugi = 0
                
                try:
                    prvi = int(s1[i][atribut])
                    drugi = int(s1[j][atribut])
                except ValueError:
                    prvi = s1[i][atribut]
                    drugi = s1[j][atribut]
                except TypeError:
                    prvi = s1[i].__getattribute__(atribut)
                    drugi = s1[j].__getattribute__(atribut)

                if prvi < drugi:
                    s[k] = s1[i]
                    i += 1 
                    kraj = 0
                else: 
                    s[k] = s1[j]  
                    j += 1  
                    kraj = 1
            k += 1 
        
        if kraj == 0:
            if k < len(s) and j < len(s1):
                s[k] = s1[j]
        elif kraj == 1:
            if k < len(s) and i < len(s1):
                s[k] = s1[i]
    else:
        i = k = 0 
        j = 1
        
        kraj = 0
        while k < len(s1)-1:  
            if i == j: 
                if kraj == 0:
                    s[k] = s1[j]  
                    j += 1 
                else:
                    s[k] = s1[i]  
                    i += 1 
            if j == len(s1)-2:
                c = i
                i = j
                j = c
            elif i == len(s1)-2:
                c = j
                j = i
                i = c

            if isinstance(atribut, int) != True:
                prvi = 0
                drugi = 0
                try:
                    prvi = int(s1[i][atribut])
                    drugi = int(s1[j][atribut])
                except ValueError:
                    prvi = s1[i][atribut]
                    drugi = s1[j][atribut]
                except TypeError:
                    prvi = s1[i].__getattribute__(atribut)
                    drugi = s1[j].__getattribute__(atribut)
                    
                if prvi < drugi:  
                    s[k] = s1[i] 
                    i += 1 
                    kraj = 0
                else:  
                    s[k] = s1[j] 
                    j += 1 
                    kraj = 1
            else:
                prvi = 0
                drugi = 0
                try:
                    prvi = int(s1[i][atribut])
                    drugi = int(s1[j][atribut])
                except ValueError:
                    prvi = s1[i][atribut]
                    drugi = s1[j][atribut]
                except TypeError:
                    prvi = s1[i].__getattribute__(atribut)
                    drugi = s1[j].__getattribute__(atribut)

                if prvi > drugi:  
                    s[k] = s1[i]  
                    i += 1 
                    kraj = 0
                else:  
                    s[k] = s1[j] 
                    j += 1  
                    kraj = 1
            k += 1
        if kraj == 0:
            if k < len(s) and j < len(s1):
                s[k] = s1[j]
        else:
            if k < len(s) and i < len(s1):
                s[k] = s1[i]
    return s

def merge_sort(s, atribut, bool_nacin_sortiranja):
    """
    :param s: lista koju je potrebno sortirati
    :param atribut: kljuc po kom da se sortira lista
    :param bool_nacin_sortiranja: True u rastucem redosledu, False u opadajucem
    """
    if len(s) > 1: 
        # podelis
        s1 = list_split(s)
        # zavladaj
        for i in s1:
            quick_sort(i, atribut, bool_nacin_sortiranja)
        # kombinuj
        s2 = []
        for i in s1[0]:
            s2.append(i)
        
        s = merge(s2, s, atribut, bool_nacin_sortiranja)
        return s
    else:
        return s
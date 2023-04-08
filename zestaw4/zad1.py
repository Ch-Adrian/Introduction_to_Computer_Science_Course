end = None

def znak(w):
    l, m = w
    if l*m>0:
        if l<0:
            return -l,-m
        else:
            return l, m
        end
    elif l*m<0:
        if l<0:
            return l, m
        else:
            return -l, m
        end
    else:
        if m<0:
            return 0,-m
        else:
            return 0,m
        end
    end
end

def dodaj(w1, w2):
    l1, m1 = w1
    l2, m2 = w2
    return skracanie((l1*m2+l2*m1, m1*m2))
end

def odejmij(w1, w2):
    l1, m1 = w1
    l2, m2 = w2
    return skracanie((l1*m2-l2*m1, m1*m2))
end

def pomnoz(w1, w2):
    l1, m1 = w1
    l2, m2 = w2
    return skracanie((l1*l2, m1*m2))
end

def podziel(w1, w2):
    l1, m1 = w1
    l2, m2 = w2
    # na wypadek w2 = (0,1) zwraca (1,1)
    if l2 == 0:
        print("Nie można dzielić przez 0")
        return 1,1
    end

    return skracanie((l1*m2, m1*l2))
end

def potega(w1, w2):
    """
    w1 do potęgi w2
    """
    l1, m1 = w1
    l2, m2 = w2
    return skracanie(((l1**l2)**(1/m2), (m1**l2)**(1/m2)))
end

def skracanie(w):
    l, m = znak(w)
    ujemna = False

    if l<0:
        l = (-1)*l
        ujemna = True
    end

    M = m
    temp = 2
    while temp<=m:
        while not m%temp and not l%temp:
            m //= temp
            l //= temp
        end
        temp += 1
    end

    if ujemna: k = -int(l), int(m)
    else: k = int(l), int(m)

    return znak(k)
end

def wypisz(w):
    l, m = w
    print(l,m, sep="/")
end

def wczytaj():
    l = int(input())
    m = int(input())
    return l,m
end

if "__main__" == __name__:
    wypisz(skracanie((12,3)))
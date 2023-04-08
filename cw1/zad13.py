end = None

l1 = int(input("Podaj liczbe pierwsza: "))
l2 = int(input("Podaj liczbe druga: "))
l3 = int(input("Podaj liczbe trzecia: "))

def NWD(a, b):
    while a != b:
        if a<b:
            b = b-a
        else:
            a = a-b
        end
    end
    return a
end

def NWW(a,b):
    return (a*b)/NWD(a,b)
end

print(int(NWW(l1, NWW(l2, l3))))
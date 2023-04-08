end = None

l1 = int(input("Podaj liczbe pierwsza: "))
l2 = int(input("Podaj liczbe druga: "))
l3 = int(input("Podaj liczbe trzecia: "))
def nwd(a, b):
    while a != b:
        if a<b:
            b = b-a
        else:
            a = a-b
        end
    end
    return a
end

print(str(nwd(l1,nwd(l2,l3))))
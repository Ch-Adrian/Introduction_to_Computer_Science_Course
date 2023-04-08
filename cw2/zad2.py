end = None

a = int(input("Podaj liczbę a: "))
b = int(input("Podaj liczbę b: "))
n = int(input("Podaj liczbę n: "))

czCalkowita = int(a/b)
a = a - b*czCalkowita
reszta = []

while len(reszta)<n:
    if a == 0:
        reszta.append(0)
    end
    
    if a<b:
        a *= 10
    else:
        t = int(a/b)
        reszta.append(t)
        a -= t*b
    end
end

wynik = str(czCalkowita) + "."
for i in reszta:
    wynik+=str(i)
end

print(wynik)
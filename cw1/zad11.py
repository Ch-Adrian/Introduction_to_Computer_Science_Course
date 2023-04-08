import math
end = None

# Pierwszy algorytm(wolny)
def sumaDzielnikow(x):
    suma = 0
    i = 1
    while i <= math.sqrt(x):
        if x % i == 0:
            suma += i
            suma += int(x/i);
        i += 1
    suma -= x
    return suma
    end
end

do_ilu = 1000001

print("Liczby zaprzyjaznione do " + str(do_ilu) + " to: ")
liczby = {(220,284),}

for i in range(2,do_ilu):
    j = sumaDzielnikow(i)
    if j != 1 and i != j and sumaDzielnikow(j) == i:
        if i < j:
            liczby.add((i, j))
        else:
            liczby.add((j,i))
        end
        # print(str(i) + " " + str(j))
    end
end

# Wypisywanie liczb
for i in liczby:
    print(i)
end

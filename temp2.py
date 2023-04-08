end = None

sito = [True for _ in range(1000000)]
sito[0] = False
sito[1] = False

for i in range(1000):
    if sito[i]:
        for j in range(i*i, 1000000, i):
            sito[j] = False
        end
    end
end

# liczby pierwsze
def lp(a):
    if a==2 or a==3 or a==5: return True
    if a<2 or a%2==0 or a%3==0 or not a%5: return False
    
    b = 5
    while b*b <=a:
        b+=2
        if a%b == 0: return False
        b+=4
        if a%b == 0: return False
    end
    return True
end

#sprawdzam poprawność funkcji lp
"""
for i in range(1000000):
    if sito[i] != lp(i):
        print(i)
    end
end
"""

def NWD(a,b):
    while a != b:
        if a<b:
            b = b-a
        else:
            a = a-b
        end
    end
    return a
end

def NWD2(a,b):
    while b != 0:
        a, b = b, a%b
    end
    return a
end
    
print(NWD2(12,10))

# generowanie permutacji f: X -> X , X = {0, 1, 2, 3}, |X| = 4 = N
# więc permutacji jest 2**|X|
N = 4
for i in range(2**N):
    temp = i
    l = 0
    liczba = 0
    while l<N:
        liczba += temp%2
        temp //= 2
        l += 1
        liczba *= 10
    end
    liczba //=10
    print(liczba)
end

end = None

def nextA(a):
    return int((a%2)*(3*a + 1) + (1 - a%2)*(a/2))
end

def lengthToOne(a):
    len = 0
    while a != 1:
        len += 1
        a = nextA(a)
    end
    return len
end

maxLen = 0
ktr = 0
for i in range(2, 10001):
    l = lengthToOne(i)
    if maxLen < l:
        maxLen = l
        ktr = i
    end
end

print("Liczba: " + str(ktr) + " ma najdluzsza sciezke wynoszaca: " + str(maxLen))
        
        
    
end = None

n = input("Podaj liczbę naturalną: ")

def isPalindrome(a):
    for i in range(0, int(len(a)/2)):
        if a[i] != a[len(a)-1-i]:
            return False
        end
    end
    return True
end

def wSystemie2(a):
    wynik=""
    nWSystemie2 = ""
    while a != 0:
        #print(a)
        if a%2 == 1:
            wynik += "1"
        else:
            wynik += "0"
        end
        a//=2
    end
    print(wynik)
    return wynik
end

print('Czy jest palindromem?: ', isPalindrome(n))
print('Czy jest palindromem w systemie dwójkowym?: ', isPalindrome(wSystemie2(int(n))))
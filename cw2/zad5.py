end = None

n = input("Liczba pierwsza(dzielna): ")
m = input("Liczba druga(dzielnik): ")

arr = []
arrLiczbyPodzielne = []

for i in range(0, len(n)):
    arr.append(0)
end

def createSetInArr(a):
    for i in range(0, len(n)):
        arr[i] = 0
    end
    
    i = 0
    a = int(a)
    while a!=0:
        if a%2 == 1:
            arr[i] = 1
            a //= 2
        else:
            arr[i]= 0
            a//=2
        end
        i += 1
    end
end

def createNumber():
    number = ""
    
    for i in range(0, len(arr)):
        if arr[i] == 1:
            number += n[i]
        end
    end
    return number
end     

for i in range(1, 2**len(n)):
    createSetInArr(i)
    num = int(createNumber())
    m = int(m)
    if num%m == 0:
        arrLiczbyPodzielne.append(num)
    end
end

print("Liczb podzielnych jest: ", len(arrLiczbyPodzielne))
for i in arrLiczbyPodzielne:
    print(i, end=", ")
    
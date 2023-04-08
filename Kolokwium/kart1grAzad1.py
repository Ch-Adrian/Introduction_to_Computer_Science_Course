end = None

a = int(input(">> "))
b = int(input(">> "))

def maxDl(a):
    temp = 0
    while a>0:
        temp+=1
        a //= 2
    end
    return temp
end

dlA = maxDl(a)
dlB = maxDl(b)

# tablica na cyfry liczby a o róznych podstawach
# długość tablicy wynosi loga + 2
Ta = [0 for _ in range(dlA+2)]

roznocyfrowe = False
podstawa = 0
while not roznocyfrowe:
    for podst in range(2, 17):
        nierozno = False
        tempA = a
        dl = 0
        while tempA > 0:
            Ta[dl] = tempA%podst
            tempA //= podst
            dl += 1
        end
        Ta[dl] = -1
        
        tempB = b
        while tempB > 0:
            reszta = tempB%podst
            for i in range(dl):
                if Ta[i] == reszta:
                    nierozno = True
                    break
                end
            end
            
            if nierozno:
                break
            end
            
            tempB //= podst 
        end
        if nierozno:
            continue
        else:
            roznocyfrowe = True
            podstawa = podst
            break
        end
    end
end

if roznocyfrowe:
    print("Znaleziona podstawa wynosi: ", podstawa)
else:
    print("Nie znaleziono podstawy")
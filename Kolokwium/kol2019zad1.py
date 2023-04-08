end = None
from random import randint
N = 12

t1 = [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
t2 = [ 1, 1, 1, 1, 1, 1, 2, 2, 2, 1, 1, 1]

def sumToPot(t1, t2):
    N = len(t1)
    # sprawdzamy każdy kawałek długości od 1 do 23 w tablicy t1
    for i in range(1, 23):
        # gdy N jest mniejsze niż 24 kawałki muszą mieścić się w tablicy
        if i>N or 24 - i > N: continue
        
        for j in range(N-i+1):
            # liczymy sumę dla kawałka [j, j+i) w tablicy t1
            # i to długość kawałka
            sum1 = 0
            k = j
            while k<j+i:
                sum1 += t1[k]
                k += 1
            end
            
            # sum1 sprawdzamy dla każdego kawałka w tablicy t2
            # l to długość kawałka
            l = 24 - i
            for m in range(N-l+1):
                # liczymy sumę sum2 dla kawałka [m, m+l)
                sum2 = 0
                n = m
                while n < m+l:
                    sum2+= t2[n]
                    n += 1
                end
                
                # sum1 + sum2 to suma dwóch kawałków w t1 i t2
                suma = sum1+sum2
                pot = 2
                while 2**pot <= suma:
                    liczba = 2
                    while liczba**pot <= suma:
                        if liczba**pot == suma:
                            print(liczba, pot)
                            return True
                        end
                        liczba += 1
                    end
                    pot += 1
                end
            end
        end
    end
    return False
end

print(sumToPot(t1, t2))
                        
                    
                    
    


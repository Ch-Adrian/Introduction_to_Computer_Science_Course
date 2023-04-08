end = None
#idx: 0,1,2,3, 4,5
T = [ 1,7,3,5,11,2 ]# tutaj (idx,war), (0, 1) + (3, 5) + (5, 2) = (8, 8) -> 8
#idx:0,1,2,3,4
U = [5,4,7,3,1]

def podzb(T):
    def find(T, idx=-1, sumEle = 0, sumIdx = 0, counter = 0):

        if counter>0 and sumEle == sumIdx :
            return counter, sumEle
        end

        if idx+1<len(T):

            a = find(T, idx+1, sumEle, sumIdx, counter)
            b = find(T, idx+1, sumEle+T[idx+1], sumIdx + idx+1, counter+1)

            if a[0]<b[0]:   return a
            else:            return b
            
        end

        return len(T), -1
    end

    if T[0] == 0:   return 0
    else:           return find(T)[1]
    end
end

print(podzb(T))
end = None

T = [2 , 2, 2, 2, 1]

def nki(T, n, icyn):
    def count(T, n, icyn, last = -1):
        if n == 0 and icyn == 1: return 1
        
        cnt = 0
        for i in range(last+1, len(T)):
            if not icyn%T[i]: 
                cnt += count(T, n-1, icyn//T[i], i)
            end
        end

        return cnt
    end

    return count(T, n, icyn)

end

print(nki(T,3, 4))

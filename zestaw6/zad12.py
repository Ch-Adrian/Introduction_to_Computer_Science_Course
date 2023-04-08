end = None

T = [2 , 2, 2, 2, 1]

def nki(T, n, icyn):
    def count(T, n, icyn, tab, last = -1):
        if n == 0 and icyn == 1:
            print(tab)
            return 1
        
        cnt = 0
        for i in range(last+1, len(T)):
            if not icyn%T[i]: 
                tab[n-1] = T[i]
                cnt += count(T, n-1, icyn//T[i], tab, i)
            end
        end

        return cnt
    end

    tab = [ 0 for i in range(n) ]
    return count(T, n, icyn, tab)

end

print(nki(T,2, 4))

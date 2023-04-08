end = None

N = 12

T=[ 0, 1, 3, 3, 4, 5 , 6, 2, 3, 4, 6, 7, 7]

def dlciagu(T):
    maxDl = 0
    for i in range(N-1):
        j = i
        eleSum = 0
        dlSum = 0
        while j< N-1 and T[j] < T[j+1]:
            eleSum += T[j]
            #print(eleSum)
            dlSum += j
            j += 1
        end
        
        dlSum += j
        eleSum += T[j]
        
        if dlSum == eleSum:
            if maxDl < j-i+1:
                maxDl = j-i+1
            end
        print(maxDl, i, j)
    end
    return maxDl
end

print(dlciagu(T))


    
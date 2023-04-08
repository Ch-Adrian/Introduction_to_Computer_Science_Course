end = None

N = 4
t = [ [ 1 for _ in range(N) ] for _ in range(N) ]

def kings(t, prev, row, suma):
    print(prev, row, suma)
    
    if row == len(t):
        if suma == 0:
            return True
        end    
    else:
        for i in range(N):
            if not (prev[0]+1>=i and prev[0]-1<=i):
                if not (prev[1] >= i and prev[1] <= i):
                    if kings(t, ( i , prev[0]), row + 1, suma + t[row][i]):
                        return True
                    end
                end
            end
        end
    end
    
    if row == 0:
        return False
    end
end

print(kings(t, (-3,-3), 0, 0))
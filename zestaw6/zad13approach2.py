end = None

def podzial(a, t=[]):
    if a == 0: print(t)
    for i in range(1, (a+1)):
        if len(t) == 0 or t[len(t)-1] <=i: podzial(a-i, t+[i])
    end
end

podzial(4)

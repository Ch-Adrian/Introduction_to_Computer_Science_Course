year = 2020

def checkSequence(a, b):
    while a < year:
        temp = a
        a = b
        b = temp + b
    if a == year:
        return True
    else: return False


def showCheckSequence(a, b):
    while a < year:
        print(a)
        temp = a
        a = b
        b = temp + b
    if a == year:
        return True
    else: return False
    
def findNumbers():
    a = 1
    b = 2
    _min = 1000000
    _a = 0
    _b = 0
    while a < year:
        while b < year:
            if checkSequence(a,b):
                if a + b < _min:
                    _min = a + b
                    _a = a
                    _b = b
            b += 1
        b = a + 2
        a += 1
    return (_min, _a, _b)

showCheckSequence(12, 52)

print(findNumbers()) #(64, 12, 52)


end = None

class Node:
    def __init__(self):
        self.val = None
        self.next = None
    end
end


class Set:
    def __init__(self):
        self.first = Node()
    end
    
    def isVal(self, ele):
        wsk = self.first.next

        while wsk!=None:
            if wsk.val == ele: return True
            wsk = wsk.next
        end

        return False
    end

    def add(self, v):
        self.remove(v)
        wsk = self.first.next
        self.first.next = Node()
        self.first.next.val = v
        self.first.next.next = wsk
    end

    def remove(self, v):
        """
        if element is present returns True, otherwise False
        """
        preWsk = self.first
        wsk = self.first.next

        while wsk != None:
            if wsk.val == v:
                preWsk.next = wsk.next
                return True
            end
            preWsk = wsk
            wsk = wsk.next
        end

        return False
    end

    def showSet(self):
        wsk = self.first.next
        t = []
        while wsk != None:
            t += [wsk.val]
            wsk = wsk.next
        end
        print(t)
    end
end

S = Set()
S.add(1)
S.add(2) 
S.showSet()
S.add(3)
S.add(4)
S.add(5)
S.showSet()
print("Sprawdzamy czy jest 3 w zbiorze")
print(S.isVal(3))
print("Usuwamy 3")
S.remove(3)
S.showSet()
print("Sprawdzamy czy jest 3 w zbiorze")
print(S.isVal(3))
print("Dodajemy powtarzający się element 4")
S.add(4)
S.showSet()
                



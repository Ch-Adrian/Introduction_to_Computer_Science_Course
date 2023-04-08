end = None

class Node:

    def __init__(self):
        self.val = None
        self.idx = None
        self.next = None
    end
end

class Array:

    def __init__(self):
        self.first = Node()
        self.last = Node()
        self.first.next = self.last
    end

    def add(self, v, n):
        preWsk = self.first

        while preWsk.next.next != None:
            if preWsk.next.idx > n:
                if preWsk.idx == n:
                    preWsk.val = v
                    return None
                else:
                    # znalezlismy miejsce i wychodzimy z petli
                    break
                end
            end
            preWsk = preWsk.next
        end

        postWsk = preWsk.next
        preWsk.next = Node()
        preWsk.next.idx = n
        preWsk.next.val = v
        preWsk.next.next = postWsk
    end

    def get(self, n):
        wsk = self.first.next

        while wsk.next != None and wsk.idx <= n:
            if wsk.idx == n:
                return wsk.val
            wsk = wsk.next
        end

        return 0
    end

    def showArray(self):
        wsk = self.first.next
        tval = []
        tidx = []
        while wsk.next != None:
            tval += [wsk.val]
            tidx += [wsk.idx]
            wsk = wsk.next
        end
        print("Val: ", tval)
        print("Idx: ", tidx)
    end

end

A = Array()

print("Dodajemy 2, 3, 4, 6")
A.add(2,2)
A.add(3,3)
A.add(4,4)
A.add(6,6)
A.showArray()
print("Dodajemy 7 pod 3")
A.add(7, 3)
A.showArray()
print("Dodajemy 1 pod 1")
A.add(1,1)
A.showArray()
print("Dodajemy 5 pod 5")
A.add(5,5)
A.showArray()
print("Pobieramy element pod 3")
print(A.get(3))
print("Pobieramy element pod 1")
print(A.get(1))
print("Pobieramy element pod 6")
print(A.get(6))
print("Pobieramy element pod 10")
print(A.get(10))
print("Pobieramy element pod -1")
print(A.get(-1))

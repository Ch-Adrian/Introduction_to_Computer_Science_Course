end = None

class Node:
    def __init__(self):
        self.val = None
        self.next = None
    end
end

class List:

    def __init__(self):
        self.first = Node()
    end

    def add(self, v):
        preWsk = self.first

        while preWsk.next != None and preWsk.next.val < v:
            preWsk = preWsk.next
        end

        postWsk = preWsk.next
        preWsk.next = Node()
        preWsk.next.val = v
        preWsk.next.next = postWsk
    end

    def remove(self, v):
        preWsk = self.first

        while preWsk.next != None and preWsk.next.val < v:
            preWsk = preWsk.next
        end

        if preWsk.next == None: return None
        if preWsk.next.val == v:
            preWsk.next = preWsk.next.next
        end
    end

    def showList(self):
        wsk = self.first.next
        t = []
        while wsk != None:
            t += [wsk.val]
            wsk = wsk.next
        end

        print(t)
    end
end

def showList(wsk):
    t = []
    while wsk != None:
        t += [wsk.val]
        wsk = wsk.next
    end
    print(t)
end

def iterMerge(wsk1, wsk2):
    
    first = None
    wsk = None
    while wsk1 != None and wsk2 != None:
        if wsk1.val < wsk2.val:
            L.add(wsk1.val)
            wsk1 = wsk1.next
        else: 
            L.add(wsk2.val)
            wsk2 = wsk2.next
        end
    end

    while wsk1 != None:
        L.add(wsk1.val)
        wsk1 = wsk1.next
    end

    while wsk2 != None:
        L.add(wsk2.val)
        wsk2 = wsk2.next
    end

    return L.first.next
end

def rekMerge(wsk1, wsk2):


L1 = List()
L2 = List()

L1.add(2)
L1.add(1)
L1.add(3)
L1.add(7)
L1.add(5)
L1.add(9)
L1.showList()
L2.add(3)
L2.add(1)
L2.add(2)
L2.add(2)
L2.add(8)
L2.add(4)
L2.add(7)
L2.add(6)
L2.showList()
showList(iterMerge(L1.first.next, L2.first.next))

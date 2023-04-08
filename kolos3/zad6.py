"""

funkcja iteruje po elementach zbioru pierwszego
i sprawdza dla każdego elementu w kolejnych zbiorach:
- czy element jest mniejszy, wtedy iteruje aż znajdzie element większy bądź równy,
gdy znajdzie takie elementy w każdym zbiorze to je porównuje
gdy są takie same to znaleźliśmy element do nowej listy

"""
end = None

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    end
end

def iloczyn(z1, z2, z3):
    lista = Node(None)
    wsk_lista = lista
    wsk_z1 = z1
    wsk_z2 = z2
    wsk_z3 = z3
    
    while wsk_z1 is not None:
        e1 = wsk_z1.val
        
        while wsk_z2 is not None and wsk_z2.val < e1:
            wsk_z2 = wsk_z2.next
        end
        
        while wsk_z3 is not None and wsk_z3.val < e1:
            wsk_z3 = wsk_z3.next
        end
        
        if wsk_z2 is not None and wsk_z3 is not None:
            if e1 == wsk_z2.val and e1 == wsk_z3.val:
                wsk_lista.next = Node(e1)
                wsk_lista = wsk_lista.next
            end
        end
        
        wsk_z1 = wsk_z1.next
    end
    
    return lista.next
end
        
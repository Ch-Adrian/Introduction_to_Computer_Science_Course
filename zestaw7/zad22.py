end = None

class Node:
	def __init__(self, v=None, n=None):
		self.val = v
		self.next = n
	end
end

def cykl(lista):
	wsk1 = lista
	wsk2 = lista.next

	while wsk1 != wsk2:
		if wsk1 is not None:
			wsk1 = wsk1.next
		end
		if wsk2 is not None:
			if wsk2.next is not None:
				wsk2 = wsk2.next.next
			else:
				wsk2 =None
			end
		end
	end

	if wsk1 is None and wsk2 is None:
		print("Lista nie ma cyklu")
	else: 
		print("Lista ma cykl")
	end
end

l = None
m = Node(1, Node(2, Node(3, Node(4, None))))
L = Node(1, Node(2, Node(3, m)))
l = L
while l.next is not None:
	l = l.next
l.next = m

cykl(L)

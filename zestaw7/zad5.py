end = None

class Node:
	def __init__(self, v=None, n=None):
		self.val = v
		self.next = n
	end
end

def zad5(list1):
	arr = [Node() for _ in range(10) ]
	wsk = [ arr[i] for i in range(10) ]
	
	while list1 is not None:
		
		kon = list1.val%10
		wsk[kon].next = list1
		wsk[kon] = wsk[kon].next
		list1 = list1.next
		wsk[kon].next = None
	
	end

	list2 = arr[0]
	wsk2 = wsk[0]
	for i in range(9):
		if arr[i+1].next is not None:
			wsk2.next = arr[i+1].next
			wsk2 = wsk[i+1]
	
	return list2.next
end

l = Node(10, Node(12, Node(13, Node(14, Node(15, Node(16, Node(17, Node(18, Node(19, Node(23, None))))))))))
l = zad5(l)
l2 = Node(17, Node(11,None))
l2 = zad5(l2)
l = l2

while l is not None:
	print(l.val)
	l = l.next

end = None

class Node:
	def __init__(self,v=None, n=None):
		self.val = v
		self.next = n
	end
end

def reverse(list1):
	list2 = Node()

	while list1 is not None:
		tmp = list2.next
		list2.next = list1
		list1 = list1.next
		list2.next.next = tmp
	end

	return list2.next
end

l = Node(1,Node(2,Node(3,Node(4,None))))
l = reverse(l)
while l is not None:
	print(l.val)
	l = l.next
end


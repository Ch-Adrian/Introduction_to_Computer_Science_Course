end = None

class Node:
	def __init__(self, v=None, n=None):
		self.val = v
		self.next = n
	end
end

def merge(list1, list2):
	list3 = Node()
	wsk = list3
	while list1 is not None and list2 is not None:
		if list1.val < list2.val:
			wsk.next = list1
			list1 = list1.next
			wsk = wsk.next
			wsk.next = None
		else:
			wsk.next = list2
			list2 = list2.next
			wsk = wsk.next
			wsk.next = None
		end
	end
	
	# list1 albo list2 nie jest równe None
	if list1 is not None:
		wsk.next = list1
	if list2 is not None:
		wsk.next = list2
	
	return list3.next
end


def rek_merge(list1, list2):
	list3 = Node()
	wsk = list3

	def rek(list1, list2, wsk):
		if list1 is not None and list2 is not None:
			if list1.val < list2.val:
				wsk.next = list1
				list1 = list1.next
				wsk = wsk.next
				wsk.next = None
			else:
				wsk.next = list2
				list2 = list2.next
				wsk = wsk.next
				wsk.next = None
			end
			return rek(list1,list2,wsk)
		else:
			if list1 is not None:
				wsk.next = list1
			if list2 is not None:
				wsk.next = list2
	
	rek(list1, list2, wsk)
	return list3.next
end

wsk1 = Node(1,Node(4,Node(6, Node(10, None))))
wsk2 = Node(2,Node(3,Node(5, None)))

a = rek_merge(wsk1, wsk2)

while a is not None:
	print(a.val)
	a = a.next
end


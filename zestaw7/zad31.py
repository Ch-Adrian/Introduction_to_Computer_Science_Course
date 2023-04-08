end = None

class Node:
	def __init__(self, v=None, n=None):
		self.val = v
		self.next = n
	end
end

# zakładam, że list_even == Node() i list_odd == Node(), oraz element o wartości 0 zawsze usuwam.
def merge(list1, list_even, list_odd):
	# list_even dodatnie parzyste
	# list_odd ujemne nieparzyste
	# ustawiam zmienne:
	del_nodes = 0
	
	node_even = list_even
	
	node_odd = list_odd

	node = list1
	
	# przechodzę po liście list1:
	while node != None:
		# dla danego wierzchołka pod wskażnikiem node pobieram jego wartość i zapisuję w v
		v = node.val
		# gdy element jest ujemny i nieparzysty:
		if v<0 and abs(v)%2==1:
			node_odd.next = node
			node = node.next
			node_odd = node_odd.next
			node_odd.next = None
		# gdy element jest dodatni i parzysty
		elif v>0 and v%2 == 0:
			node_even.next = node
			node = node.next
			node_even = node_even.next
			node_even.next = None
		# tutaj usuwamy elementy
		else:
			del_nodes += 1
			tmp = node
			node = node.next
			tmp.next = None
		end
	end

	return del_nodes
end

#===== test 1 =========
print("Test 1")
l = Node(-1, Node(2, Node(3, Node(4, None))));
# tworzę wskaźniki i dopisuję im puste elementy(wartowniki), bo samego wskaźnika nie da się 
# przekazać do funkcji, ponieważ funkcja skopiuje jego wartość do swojej wartości. Czyli
# gdyby l_even = None to po przekazaniu funkji merge list_even też równa się None. Funkcja 
# na końcu nie ma jak zwrócić z powrotem obiektu(listy) do wskażnika l_even, 
# więc gdy do wskażnika l_even odrazu przypiszemy obiekt Node() to w funkcji merge
# wskażnik list_even skopiuje adres do obiektu i będzie wskazywał na już utworzony obiekt listy.
# Wtedy w funkcji poszczególne elementy będą dopisywane do tego obiektu( czyli do tego samego co
# wskazuje wskażnik l_even który jest poza funkcjią) i funkcja merge nie musi się przejmować
# przekazywaniem listy utworzonej do wskażnika l_even.
# Tutaj daję taki komentarz, bo te zadania są chyba robione pod programowanie w C++, a tam można
# właśnie tak przypisywać wskażniki i wtedy l_even by mogło być równe None ;)
l_even = Node()
l_odd = Node()

# wyrzucamy 3, więc wynik to 1
print("Liczba elementów wyrzuconych: ", merge(l, l_even, l_odd))

# l_even:
l_even = l_even.next
while l_even is not None:
	print(l_even.val, end=" ")
	l_even = l_even.next
print()

# l_odd:
l_odd = l_odd.next
while l_odd is not None:
	print(l_odd.val, end=" ")
	l_odd = l_odd.next
print()

#======= test 2 =========
print("Test 2")
l = Node(-2, Node(-1, Node(0, Node(1,Node(2,None)))))
l_even = Node()
l_odd = Node()

# wyrzucamy -2, 0, 1, więc wynik to 3
print("Liczba elementów wyrzuconych: ", merge(l, l_even, l_odd))

# l_even:
l_even = l_even.next
while l_even is not None:
	print(l_even.val, end=" ")
	l_even = l_even.next
print()

# l_odd:
l_odd = l_odd.next
while l_odd is not None:
	print(l_odd.val, end=" ")
	l_odd = l_odd.next
print()

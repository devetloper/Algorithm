###make node, LinkedList ###
class Node:
	def __init__(self,data = None, prev = None, next = None):
		self.data = data
		self.prev = prev
		self.next = next

class LinkedList:
	def  __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

### make list function ###
def add_list(lst,arr):
	#link between Node
	first = last = Node(arr[0])
	for val in arr[1:]:
		new = Node(val,last)
		last.next = new
		last = new
	
	#make first list
	if lst.head is None:
		lst.head = first
		lst.tail = last
	
	#put array into list
	else:
		cur = lst.head # cur = current Node
		while cur is not None:
			if cur.data > arr[0]:
				break
			cur = cur.next
		
		if cur is None: #attach array into backend
			first.prev = lst.tail
			lst.tail.next = first
			lst.tail = last
		
		elif cur.prev is None: #attach array into frontend
			last.next = lst.head
			lst.head.prev = last
			lst.head = first
		
		else: #put array in list
			prev = cur.prev
			first.prev = prev
			prev.next = first
			last.next = cur
			cur.prev = last
	lst.size += len(arr)

###make print list function ###
def print_list(lst):
	count = 10
	cur = lst.tail
	while count:
		print(cur.data, end=" ")
		cur = cur.prev
		count -= 1
	print()
		
		

###input###
T = int(input())
for test_case in range(1, T + 1):
	n, m = map(int,input().split())
	arrays = [list(map(int,input().split())) for _ in range(m)]

	linked_list = LinkedList()
	for arr in arrays:
		add_list(linked_list,arr)
	
	print(f"#{test_case}", end= " ")
	print_list(linked_list)



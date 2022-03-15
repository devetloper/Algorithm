# Solving , Have to add remove, change , find function

###single Linked List###
class Node:
	def __init__(self,data = None, next= None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

###convert array to Linkedlist ###
def covert_linked_list(arr):
	linked_list = LinkedList()
	first = last = Node(arr[0])
	for val in arr[1:]:
		new = Node(val)
		last.next = new
		last =new
	
	linked_list.head = first
	return linked_list

### print Function for test###	
def print_list(lst):
	cur = lst.head
	while True:
		if cur is None:
			break
		print(cur.data, end= " ")
		cur = cur.next

### Function insert ###
def insert(idx,val):
	global mylist
	cnt = 0
	cur = mylist.head
	while cnt != idx - 1:
		cur = cur.next
		cnt += 1
	new = Node(val,cur.next)
	cur.next = new

### Function remove ###
def remove(idx):
    pass
### Function change ###
def change(idx,val):
    pass
### Function find ###
def find(idx):
    pass
			
### input ###
l,m,n = map(int,input().split())
first_arr =list(map(int,input().split()))

to_do_list =[]
for _ in range(m):
	to_do_list.append(list(input().split()))

for to_do in to_do_list:
	if to_do[0] == 'D':
		to_do[1] = int(to_do[1])
	
	elif to_do[0] == 'I' or to_do[0] =="C":
		to_do[1] = int(to_do[1])
		to_do[2] = int(to_do[2])

mylist = covert_linked_list(first_arr)
insert(2,7)
print_list(mylist)

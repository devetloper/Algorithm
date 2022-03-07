'''
To make List
1. Node class
2. Linked list class
3. Append method
4. Length method
5. Display method
6. GetData method
7. Erase method
8. Insert method
'''

#1
class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

#2
class LinkedList:
    def __init__(self):
        self.head = Node() #No data, idx

    #3
    def Append(self, data):
        new_node= Node(data)
        curn = self.head
        while curn.next != None:
            curn = curn.next
        curn.next = new_node
    
    #4
    def Length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            total += 1
            cur = cur.next
        return total
    
    #5
    def Display(self):
        display = []
        cur = self.head
        while cur.next != None:
            cur = cur.next
            display.append(cur.data)
        print(display)

linkedlist = LinkedList()
linkedlist.Append(3)
linkedlist.Append(4)
linkedlist.Display()
            



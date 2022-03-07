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

    #6
    def GetData(self,idx):
        if idx >= self.Length():
            print("Error")
            return None
        cur_idx =0
        cur_node = self.head
        while True:
            cur_node = cur_node.next
            if cur_idx == idx:
                print (cur_node.data)
                break
            cur_idx += 1
            
    #7
    def Erase(self,idx):
        if idx >= self.Length():
            print("Error")
            return None
        cur_idx = 0
        cur = self.head
        while True:
            last_node = cur
            cur = cur.next
            if cur_idx == idx:
                last_node.next = cur.next
                return
            cur_idx += 1 



test = LinkedList()
test.Append(0)
test.Append(1)
test.Append(2)
test.Append(3)
test.Display()
test.GetData(2)
test.Erase(2)
test.Display()



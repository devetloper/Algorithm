class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
class Tree:
    def __init__(self):
        self.route = None

mytree = Tree()
a = Node(2)
for i in range(3):
    a.left = Node(i+7)
    a= a.left



print(a.left.data)
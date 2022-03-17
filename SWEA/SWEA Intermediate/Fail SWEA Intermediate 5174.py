

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

class Tree:
    def __init__(self):
        self.route = None

e, n = map(int,input().split())
line_pair = list(map(int,input().split()))

parents = []
children = []

for i in range(len(line_pair)):
    if i % 2 == 0:
        parents.append(line_pair[i])
    else:
        children.append(line_pair[i])


node_lst = [i+1 for i in range(e+1)]

mytree = Tree() 
for num in node_lst:
    if num not in children:
        mytree.route = Node(num)

mytree.route.left = Node(1)
Node(1).left = Node(3)

print(mytree.route.data)
print(mytree.route.left.data)
# print(parents)
# print(children)



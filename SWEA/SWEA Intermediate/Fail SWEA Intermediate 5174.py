class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


e, n = map(int,input().split())
line_pair = list(map(int,input().split()))

parents = []
children = []

for i in range(len(line_pair)):
    if i % 2 == 0:
        parents.append(line_pair[i])
    else:
        children.append(line_pair[i])

tree = {}

for i in range(len(parents)):
    if parents[i] not in tree:
        tree[parents[i]] = Node(parents[i],children[i])
    else:
        tree[parents[i]].right = children[i]

def pre_order(node):
    try:
        print(node.data)
        if node.left != None:
            pre_order(tree[node.left])
        if node.right != None:
            pre_order(tree[node.right])
    except KeyError:
        pass

pre_order(tree[2])
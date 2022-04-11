### Now Solving have to complete function ###
from collections import deque

def find_node(start,goal):
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        ### have to complete function ###

v, e = map(int,input().split())

node_list = [[] for _ in range(v + 1)] #node list

for  _ in range(e):
    a, b = map(int,input().split())
    node_list[a].append(b)

s, g = map(int,input().split())

ans = find_node(s,g)
print(ans)


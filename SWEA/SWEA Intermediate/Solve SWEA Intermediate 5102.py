from collections import deque

def find_node(start,goal):
    dist = [0 for _ in range(v + 1)]
    q = deque()
    q.append(start)
    while q:
        node = q.popleft()
        if node_list[node] != []:
            for i in node_list[node]:
                if i == goal:
                    return dist[node] + 1
                else:
                    node_list[i].remove(node)
                    q.append(i)
                    if dist[i] ==0:
                        dist[i] = dist[node] + 1
    return 0

T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int,input().split())

    node_list = [[] for _ in range(v + 1)] #node list

    for  _ in range(e):
        a, b = map(int,input().split())
        node_list[a].append(b)
        node_list[b].append(a)

    s, g = map(int,input().split())

    ans = find_node(s,g)
    print(f"#{test_case}",ans)


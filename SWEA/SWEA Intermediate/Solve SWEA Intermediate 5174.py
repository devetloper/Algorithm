def count_tree(n):
    if n <= 0:
        return
    global cnt
    cnt += 1
    if left[n-1]:
        count_tree(left[n-1])
    if right[n-1]:
        count_tree(right[n-1])

#### input ###
T = int(input())
for test_case in range(1, T + 1):
    e, n = map(int,input().split())
    line_pair = list(map(int,input().split()))

    parents = []
    children = []

    for i in range(len(line_pair)):
        if i % 2 == 0:
            parents.append(line_pair[i])
        else:
            children.append(line_pair[i])

    ### make left, right list ###
    left = [0 for i in range(e+1)]
    right = [0 for i in range(e+1)]

    for i in range(len(parents)):
        if left[(parents[i] -1)]:
            right[(parents[i] -1)] = children[i]
        else:
            left[(parents[i] -1)] = children[i]

    cnt = 0
    count_tree(n)
    print(f"#{test_case}",cnt)
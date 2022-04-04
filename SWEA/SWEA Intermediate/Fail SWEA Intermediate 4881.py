def backtracking(r,v,s):
    global min
    if r == 3:
        if s < min:
            min = s
        return
    if s > min:
        return
    for i in range(n):
        if not v[i]:
            v[i] = 1
            s += numbers[r][i]
            r += 1
            backtracking(r,v,s)
            r -= 1
            s -= numbers[r][i]
            v[i] = 0
            
n = int(input())
numbers =[]
for _ in range(n):
    row = list(map(int,input().split()))
    numbers.append(row)

min=99**99
visited = [0 for _ in range(n)]
bt = backtracking(0,visited,0)
print(min)

def backtracking(r= 0,v=[],s=0):
    global min
    if r == 3:
        if s < min:
            min = s
        return
    for i in range(n):
        s += numbers[r][i]
        v.append(i)
        r += 1
        backtracking(r,v,s)


n = int(input())
numbers =[]
for _ in range(n):
    row = list(map(int,input().split()))
    numbers.append(row)

min=99**99
s = backtracking(0,[],0)
print(min)

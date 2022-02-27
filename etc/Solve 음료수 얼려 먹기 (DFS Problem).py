def dfs(x,y):
    if x <= -1 or y<= -1 or x >= n or y >= n: # If Range of searching out of index, return Fail and stop
        return False
    
    if tray[x][y] == 0:  #tray[x][y] ==0 -> not visited, can pour drink
        tray[x][y] = 1   # cannot pour drink, visited #No need to be 1, just Not 0
        dfs(x-1,y)       # search up, right,down,left and return None, just change tray value into 1(visitied) 
        dfs(x,y+1)
        dfs(x-1,y)
        dfs(x,y-1)
        return True
    return False # if x,y in range, tray[x][y] ==1 


### input ###
n, m = map(int,input().split())

tray = []
for _ in range(n):
    row_str = input()
    row = []
    for num in row_str:
        row.append(int(num))
    tray.append(row)

# result += 1 if dfs funtion return True
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j):
            result += 1

print(result)
### input ###
n, m = map(int,input().split())

tray = []
for _ in range(n):
    row_str = input()
    row = []
    for num in row_str:
        row.append(int(num))
    tray.append(row)

visited_list = []
for i in range(n) :
    for j in range(m):
        if tray[i][j] == 0:
            visited_list.append([i,j])

visited_bool = [[False for i in range(n)] for j in range(m)]

stack = []

for cord in visited_list:
    x, y = cord
    if visited_bool[x][y] == False:
        stack.append(cord)
        visited_bool[x][y] = True
        while True:
            try:
                if [x+1,y] in visited_list:
                    stack.append([x+1,y])
                    visited_bool[x+1][y] = True
                if [x-1,y] in visited_list:
                    stack.append([x-1,y])
                    visited_bool[x-1][y] = True
                if [x,y+1] in visited_list:
                    stack.append([x,y+1])
                    visited_bool[x][y+1] = True
                if [x,y-1] in visited_list:
                    stack.append([x,y-1])
                    visited_bool[x][y-1] = True
            
            except IndexError:
                pass

print(stack)

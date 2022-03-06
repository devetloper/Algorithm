def is_safe(y,x):
    return 0 <=y < n and 0 <= x <n and (maze[y][x] == 0 or maze[y][x] ==3)

def move(y, x):
    global ans 

    if maze[y][x] ==3:
        ans = 1
        return
    
    visited.append((y,x))
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    for i in range(4):
        go_y = y + dy[i]
        go_x = x + dx[i]
        if is_safe(go_y,go_x) and (go_y,go_x) not in visited:
            move(go_y, go_x)

### input ###
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())

    maze =[]
    for i in range(n):
        maze.append(list(map(int,input()))) 

    for i in range(n):
        for j in range(n):
            if maze[i][j] == 2:
                start = [i,j]



		
    ans = 0
    visited = []
    start_y, start_x = start
    move(start_y, start_x)
    print(f"#{test_case}",ans)

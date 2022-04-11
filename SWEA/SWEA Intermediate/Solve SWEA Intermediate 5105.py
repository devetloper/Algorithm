from collections import deque

def bt(sx,sy,gx,gy):
	q = deque()
	q.append((sx,sy))
	visited[sx][sy] = True
	while q:
		x,y = q.popleft()
		for i in range(4):
			if x + dx[i] >= n or x + dx[i] < 0 or y + dy[i] >= n or y + dy[i] < 0:
				continue
			if x+ dx[i] == gx and y + dy[i] == gy:
				return maze[x][y] 
			if not visited[x+ dx[i]][y + dy[i]] and maze[x+ dx[i]][y + dy[i]] == 0 :
				q.append((x+ dx[i], y +dy[i]))
				visited[x+ dx[i]][y + dy[i]] = True
				if x == sx and y == sy:
					maze[x+ dx[i]][y + dy[i]] = 1
				else:
					maze[x+ dx[i]][y + dy[i]] = maze[x][y] + 1
	return 0
	
T = int(input())
for test_case in range(1, T + 1):	
	n = int(input())

	maze = []
	for _ in range(n):
		maze.append(list(map(int,input())))

	for i in range(n):
		for j in range(n):
			if maze[i][j] == 2:
				start_x,start_y = [i,j]

	for i in range(n):
		for j in range(n):
			if maze[i][j] == 3:
				goal_x,goal_y = [i,j]

	visited = [[False for _ in range(n)] for _ in range(n)]

	dx = [-1,0,1,0]
	dy = [0,1,0,-1]



	btr = bt(start_x,start_y,goal_x,goal_y)
	print(f"#{test_case}",btr)



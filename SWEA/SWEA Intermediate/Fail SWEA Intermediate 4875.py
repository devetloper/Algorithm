### input ###
n = int(input())

maze =[]
for i in range(n):
    maze.append(list(map(int,input()))) # make input code more simply

for i in range(n):
    for j in range(n):
        if maze[i][j] == 2:
            start = [i,j]
        if maze[i][j] == 3:
            goal = [i,j]

stack = []

def search(x,y):
    if maze[i][j] ==3 or ans:
        pass

def move(x,y):
	if search(x,y):
		pass 	# move and put in stack
		

ans = 0

start_x, start_y = start
print(start_x,start_y)


### input ###
#n = int(input())

#maze =[]
#for i in range(n):
    #maze.append(list(map(int,input()))) # make input code more simply

maze = [[1,3,1,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,0,1,0,1],[1,0,0,2,1]]
n=5

for i in range(n):
    for j in range(n):
        if maze[i][j] == 2:
            start = [i,j]
        if maze[i][j] == 3:
            goal = [i,j]

stack = []

def search(x,y):
	try:
		if maze[x-1][y] or maze[x][y+1] or maze[x+1][y] or maze[x][y-1] == 3:
			return 1
		
		elif maze[x-1][y] == 0:
			return [x-1,y]
		
		elif maze[x][y+1] == 0:
			return [x,y+1]
		
		elif maze[x+1][y] == 0:
			return [x+1,y]
		
		elif maze[x][y-1] == 0:
			return [x,y-1]
		
		else:
			return False
			
	except IndexError:
		print(5)
					
start_x, start_y = start
print(start_x,start_y)
print(goal)
print(search(start_x,start_y))


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
	pass # if 0 or 3 in up,right,down,left return True

def move(x,y):
	if search(x,y):
		pass 	# move and put in stack
		
					
start_x, start_y = start
print(start_x,start_y)
print(goal)
print(search(start_x,start_y))


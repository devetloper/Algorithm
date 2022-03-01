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


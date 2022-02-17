######### Fail with 8/10 of Test case #########
T = int(input())

for test_case in range(1, T + 1):
    n = int(input())

    maze =[]
    for i in range(n):
        row = input()
        row_list =[1]
        for j in row:
            row_list.append(int(j))
        row_list.append(1)
        maze.append(row_list)
    maze.insert(0, [1 for i in range(n+2)]) 
    maze.insert(n+1, [1 for i in range(n+2)])

    for i in range(1,n+1):
        for j in range(1,n+1):
            if maze[i][j] == 2:
                start_x, start_y = i,j

    for i in range(1,n+1):
        for j in range(1,n+1):
            if maze[i][j] == 3:
                goal_x, goal_y = i,j
    ### make list that each idx can go ###
    can_go = [[[] for i in range(n+2)] for i in range(n+2)]   ### make empty list  ###

    for i in range(1,n+1):  ### append cordinate when not 1(wall) ###
        for j in range(1,n+1):
            if maze[i][j] != 1:
                if maze[i+1][j] != 1:
                    can_go[i][j].append([i+1,j])
                if maze[i][j+1] != 1:
                    can_go[i][j].append([i,j+1])
                if maze[i-1][j] != 1:
                    can_go[i][j].append([i-1,j])
                if maze[i][j-1] != 1:
                    can_go[i][j].append([i,j-1])

    ### stack ###

    stack =[]

    def push_item(x):
        stack.append(x)

    def pop_item():
        return stack.pop(-1)

    ### make move function ###
    def move(x,y):
        try:
            if len(can_go[x][y]) != 0:
                for route_x, route_y in can_go[x][y]:
                    if [goal_x, goal_y] in can_go[route_x][route_y]:
                        return 1
                    
                    else:
                        push_item([x,y])
                        for route_x, route_y in can_go[x][y]:
                            can_go[x][y].remove([route_x,route_y])
                            return move(route_x, route_y)
            
            elif len(can_go[x][y]) == 0:
                poped_x, poped_y = pop_item()
                return move(poped_x, poped_y)
        
        except IndexError:
            return 0



    print(f"#{test_case}",move(start_x, start_y))


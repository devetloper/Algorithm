given_list = [12, 24, 35, 70, 88, 120, 155]

out_list = [given_list[i-1] for i in (1,5,6)]

goal_list =[i for i in given_list if i not in out_list]


print(goal_list)
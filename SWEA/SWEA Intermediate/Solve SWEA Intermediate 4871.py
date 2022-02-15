T = int(input())

for test_case in range(1, T + 1):
	v, e = map(int,input().split())

	### make list that v can go ###
	can_go = [[] for i in range(v)]
	for i in range(e):
		start, end = map(int,input().split())
		can_go[start - 1].append(end)

	s, g = map(int,input().split())
	s -= 1

	### make stack function ###
	stack = []
	def push_item(x):
		stack.append(x)

	def pop_item():
		return stack.pop(-1)

	push_item(s)
	###  finding route   ###
	def find_route(start, goal, route_list):
		try:	
			if goal in route_list[start]:                 ### way to goal
				return 1
			else:
				if len(route_list[start]) == 0:
					return find_route(pop_item(), goal, route_list) 
				else:
					for route in route_list[start]:
						if len(route_list[route - 1]) == 0:    ### no way to go
							route_list[start].remove(route)
							return find_route(pop_item(),goal,route_list)
						else:                                 ### way to go
							push_item(route -1)
							return find_route(route -1,goal,route_list)
		except IndexError:
			return 0

#!!! have to return 0 when no way to goal
	print(f"#{test_case}",find_route(s,g,can_go))

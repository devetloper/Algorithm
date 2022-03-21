def make_tree(node):
	global cnt
	if left[node-1]:
		#print(left[node-1])
		make_tree(left[node-1])
	cnt += 1
	node_lst.append(node)
	if right[node-1]:
		#print(right[node-1])
		make_tree(right[node-1])

T = int(input())
for test_case in range(1, T + 1):
	n = int(input())

	left = []
	right = []
	for i in range(1,n+2):
		if (2*i) <= n:
			left.append(2*i)
			if (2*i +1) <=n:
				right.append((2*i +1))
		else:
			left.append(0)
			right.append(0)
	#print(list(i for i in range(1,n+1)))
	#print(left)
	#print(right)

	node_lst = []
	cnt = 0

	make_tree(1)
	#print(node_lst)
	print(f"#{test_case}", end= " ")
	print(node_lst.index(1)+1, end= " ")
	print(node_lst.index(n//2) + 1)


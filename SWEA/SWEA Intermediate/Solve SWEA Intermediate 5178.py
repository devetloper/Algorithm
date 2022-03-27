###input###
T = int(input())
for test_case in range(1, T + 1):
	n, m, l = map(int,input().split())
	node_data = {}
	for _ in range(m):
		node, data = map(int,input().split())
		node_data[node] = data

	###make tree with leaf ###
	tree = [0 for i in range(n)]
	for node,data in node_data.items():
		tree[node -1] = data

	### make parents ###
	parents_num = list(range(n-m))
	parents_num.reverse()
	for i in parents_num:
		if (2*i + 2) <= len(tree) -1:
			tree[i] = tree[2*i + 1] + tree[2*i + 2]
		else:
			tree[i] = tree[2*i + 1]

	print(f"#{test_case}",tree[l-1])



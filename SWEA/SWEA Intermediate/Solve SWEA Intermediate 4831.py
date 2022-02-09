T = int(input())
for test_case in range(1, T + 1):
    ################# make bus stop ########################
	k, n, m = map(int,input().split(" "))

	bus_stop = [0]* (n +1)

	charge = input().split(" ")

	int_charge =[]
	for i in charge:
		int_charge.append(int(i))

	bus_stop[0] = int_charge[0]

	dist_li = []
	for i in range(len(int_charge)-1):
		dist = int_charge[i+1] - int_charge[i]
		dist_li.append(dist)
	dist_li.append(n - int_charge[-1])

	for i in range(len(int_charge)):
		bus_stop[int_charge[i]] = dist_li[i]

################# make move ########################

	gas = k
	bus = 0
	fill_gas = 0

	while bus <= n:
		if gas ==0 and bus_stop[bus] == 0 and bus != n:
			fill_gas = 0
			break

		elif gas < bus_stop[bus] and bus_stop[bus] != 0:
			gas = k - 1
			bus += 1
			fill_gas += 1
	
		else:
			gas -= 1
			bus += 1



	print(f"#{test_case} {fill_gas}")


T = int(input())
for test_case in range(1, T + 1):
#######make band#########
	n, m =map(int,input().split(" "))

	pre_band = input().split(" ")

	band =[]
	for i in pre_band:
		if i != "":
			band.append(int(i))
	
	######make total list###########
	totals = []
	for i in range(len(band)-(m-1)):
		total =0
		for j in range(m):
			total += band[i + j]
		totals.append(total)

	sorted_totals = sorted(totals)

	print(f"#{test_case} {sorted_totals[-1] - sorted_totals[0]}")


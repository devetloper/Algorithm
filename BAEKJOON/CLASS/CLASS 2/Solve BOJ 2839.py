n = int(input())

max_5 = n //5

ans = -1
for i in range(max_5,-1,-1):
	if (n - (i * 5)) % 3 ==0:
		num_5 = i
		num_3 = int((n - (i * 5)) / 3 )
		ans = (num_5 + num_3)
		break
print(ans)


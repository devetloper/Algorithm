a, b = map(int,input().split())
for i in range(a,0,-1):
	if a % i ==0 and b % i ==0:
		c = i
		break

print(i)
if a > b:
	print(int(a / i * b))
else:
	print(int(b / i * a))


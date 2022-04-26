a,b,v = map(int,input().split())

num = (v-a)/(a-b)
if (num * 10) % 10 == 0:
	ans = int(num) + 1
else:
	ans = int(num) + 2
print(ans)


def bt(idx, visited, sum):
	global ans
	
	if sum > m:
		return
	elif idx == 3:
		if sum > ans:
			ans = sum 
	else:
		for i in range(n):
			if not visited[i]:
				visited[i] = 1
				bt(idx + 1,visited,sum + numbers[i])
				visited[i] = 0
				

n , m = map(int,input().split())
numbers = list(map(int,input().split()))

visited = [0 for _ in range(n)]
ans = 3
sum = 0
bt(0,visited,sum)
print(ans)


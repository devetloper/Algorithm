x=int(input())
a=[]
for i in range(1,x+1):
	if x%i==0:
		a.append(i)
for i in a:
	print("%d(은)는 %d의 약수입니다." %(i,x))
if len(a)==2:
	print("%d(은)는 %d과 %d로만 나눌 수 있는 소수입니다." %(x, a[0],a[1]))

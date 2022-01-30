def pallindrome(x):
	x_li=list(x)
	a=["0"]*len(x_li)
	for i in range(len(x_li)):
		a[-(i+1)]=x_li[i]
	return a
		
x=input()
p="".join(pallindrome(x))
print(p)
if x==p:
	print("입력하신 단어는 회문(Palindrome)입니다.")


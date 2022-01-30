man1=input()
man2=input()

def rcp(x,y):
	if x==y:
		print("draw")
	elif (x=="바위"and y=="가위") or (x=="가위" and y=="보") or (x=="보" and y=="바위"):
		print("%s가 이겼습니다!" %x)
	else:
		print("%s가 이겼습니다!" %y)

x=input()
y=input()

rcp(x,y)


x,y=input().split(", ")
def longer(x,y):
	x_li=list(x)
	y_li=list(y)
	if len(x_li)>len(y_li):
		print(x)
	else:
		print(y)
	
longer(x,y)


T= int(input())
for _ in range(T):
	h,w,n= map(int,input().split())
	
	floor = n % h
	if floor ==0:
		floor_str = str(h)
	else:
		floor_str = str(floor)
		
	if n % h ==0:
		room = n // h
	else:
		room = n // h + 1
		
	if room < 10:
		room_str = "0"+str(room)
	else:
		room_str = str(room)
			
	print(floor_str+room_str)


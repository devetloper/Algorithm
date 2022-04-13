x,y,w,h = map(int,input().split())

distance = [x,y,w-x,h-y]
min_distance = min(distance)
print(min_distance)


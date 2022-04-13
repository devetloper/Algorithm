from unittest import result


numbers = []
while True:
    x,y,z = map(int,input().split())
    if x ==0 and y==0 and z==0:
        break
    else:
        numbers.append([x,y,z])

results = []
for number in numbers:
    sorted_number = sorted(number)
    if sorted_number[0] ** 2 + sorted_number[1] ** 2 == sorted_number[2] **2:
        results.append("right")
    else:
        results.append("wrong")

for result in results:
    print(result)

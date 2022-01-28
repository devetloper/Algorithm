a=[]
for i in range(1,101):
    if i%2==1:
        a.append(i)
for i in range(len(a)-1):
    print(a[i], end=", ")
print(a[-1])


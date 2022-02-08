a=range(1,11)
b=filter(lambda x: x%2==0, a)
c=map(lambda x: x**2, b)
print(list(c))


url = input().split("/")

del url[1]
url[0] = url[0].rstrip(":")

print(f"protocol: {url[0]}")
print(f"host: {url[1]}")
print(f"others: {url[2]}")


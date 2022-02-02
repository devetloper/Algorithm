line = "abcdef"
def make_dict(x):
	dic = {}
	for i in range(len(line)):
		dic[line[i]] = i
	return dic
dic = make_dict(line)
for alp,num in dic.items():
	print(alp, num, sep=": ")


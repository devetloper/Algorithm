price_dic = {"TV" :2000000, "냉장고":1500000, "책상":350000, "노트북" :1200000, "가스레인지" :200000, "세탁기" :1000000}

sorted_price_dic = sorted(price_dic.items(), key= lambda item: item[1], reverse = True)

for i in sorted_price_dic:
	print("{0}: {1}".format(i[0],i[1]))


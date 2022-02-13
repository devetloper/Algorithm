
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
	def search_bin(start,end ,find_page,count=0):
			
		if  int((start + end) / 2) == find_page:
			count  += 1
			return count
		
		elif find_page < int((start + end) / 2):
			count += 1
			return search_bin(start,int((start + end) / 2),find_page,count)
			
		elif find_page > int((start + end) / 2):
			count += 1
			return search_bin(int((start + end) / 2) ,end, find_page,count)

		
	total_page , a , b = map(int,input().split(" "))

	a_num = search_bin(1, total_page, a)
	b_num = search_bin(1, total_page, b)

	if a_num > b_num:
		print(f"#{test_case} B")

	elif a_num < b_num:
		print(f"#{test_case} A")

	else:
		print(f"#{test_case} 0")


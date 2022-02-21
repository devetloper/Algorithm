T = int(input())

for test_case in range(1, T + 1):
	### rcp function ###
	def rcp(x,y):
		if card_dict[x] == card_dict[y]:
			if x < y:
				return x
			else:
				return y
		
		elif card_dict[x] == 1 and card_dict[y] == 3:
			return x

		elif card_dict[x] == 3 and card_dict[y] == 1:
			return y

		elif card_dict[x] > card_dict[y]:
			return x
			
		else:
			return y

	### group ###
	def group(group_list):

		if len(group_list) == 1:
			return group_list[0]
			
		
		elif len(group_list) == 2:
			return rcp(group_list[0],group_list[1])
			
		else:
			i = group_list[0]
			j = group_list[-1]
			cut = group_list.index((i+j)//2)
			left = group(group_list[:cut+1])
			right = group(group_list[cut+1:])
			winner = rcp(left,right)
			return winner

	###input###
	n = int(input())

	cards = input().split(" ")

	card_dict = {i:int(cards[i-1]) for i in range(1,n+1)}

	### output###
	students = [key for key in card_dict]
	print(f"#{test_case}",group(students))


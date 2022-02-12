T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

	###make board ######

	board = [[0 for i in range(10)] for j in range(10)]


	######input square######
	num_square = int(input())

	cord_colors =[]
	for i in range(num_square):
		cord_color = input().split(" ")
		cord_colors.append(cord_color)

	####make cord =((2,2),(3,3)) ,color= 1 type###
	input_cord_colors =[]
	for cord_color in cord_colors:
		
		cord_lu = (int(cord_color[0]),int(cord_color[1]))
		
		cord_rd = (int(cord_color[2]),int(cord_color[3]))
		
		color = int(cord_color[4])
		
		input_cord_colors.append((cord_lu,cord_rd,color))

		
	########draw square######

	def draw(cord,color):
		for i in range(cord[0][1] , cord[1][1] + 1):
			for j in range(cord[0][0] , cord[1][0] +1):
				
				if board[i][j] == 3:
					pass
				
				elif board[i][j] != color:
					board [i][j] += color
		
		return board
	for i in input_cord_colors:
		draw([i[0],i[1]],i[2])
				

	######calculate area########

	count = 0
	for i in range(10):
		for j in range(10):
			if board[i][j] == 3:
				count += 1

	print("#{0} {1}".format(test_case, count))


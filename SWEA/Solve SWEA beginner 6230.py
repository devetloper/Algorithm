score={1:88,2:30,3:61,4:55,5:95}

for stu,score_num in score.items():
	if score_num>=60:
		print("%d번 학생은 %d점으로 합격입니다." %(stu,score_num))
	else:
		print("%d번 학생은 %d점으로 불합격입니다." %(stu,score_num))


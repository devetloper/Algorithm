def make_total(x):
	total=0
	for i in x:
		total += i
	return total
		
scores = []

score_1 = (90,80)
score_2 = (85,75)
score_3 = (90,100)

scores.append(score_1)
scores.append(score_2)
scores.append(score_3)

	
for idx,score in enumerate(scores):
	total = make_total(score)
	print("{0}번 학생의 총점은 {1}점이고, 평균은 {2:0.1f}입니다.".format(idx + 1,total,total/len(score)))


line="ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC"
line_li=list(line)
score_dic={"A":4,"B":3,"C":2,"D":1}
score=list(map(lambda x: int(score_dic[x]),line_li))
total=0
for i in score:
	total+=i
print(total)


class Student():
	
	def __init__(self,kor,eng,mat):
		self.__kor = kor
		self.__eng= eng
		self.__mat = mat
		
	def make_total(self):
		self.__total = self.__kor + self.__eng + self.__mat
		
		return self.__total
		
kor, eng, mat = map(int,input().split(","))

a= Student(kor,eng,mat)
print("국어, 영어, 수학의 총점: {0}".format(a.make_total()))


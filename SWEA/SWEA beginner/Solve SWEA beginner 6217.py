# get help
class Student():
	
	def __init__(self, name):
		self.__name = name
	
	@property
	def name(self):
		return self.__name
	
	def __repr__(self):
		return (f"이름: {self.__name}")


class GraduateStudent(Student):
	
	def __init__(self,name,major):
		super().__init__(name)
		self.__major = major
	
	
	@property
	def major(self):
		return self.__major
		
	def __repr__(self):
		return f'이름: {self.name}, 전공: {self.major}'

hong = Student("홍길동")
lee = GraduateStudent("이순신", "컴퓨터")
print(hong)
print(lee)


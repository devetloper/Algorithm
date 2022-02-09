class Person():
	
	def getGender(self):
		return "Unknown"
		
class Male(Person):
	
	def getGender(self):
		return "Male"

class Female(Person):
	
	def getGender(self):
		return "Female"

man = Male()
print(man.getGender())

woman = Female()
print(woman.getGender())



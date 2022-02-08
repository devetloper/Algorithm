from math import pi

def cut_float(num,idx):
	str_num = str(num)
	num_2f_str = str_num[:str_num.find(".")+(idx +1)]
	return num_2f_str

class Circle():
	
	def __init__(self,radius):
		self.radius = radius
	
	def surface_circle(self):
		return self.radius ** 2 * pi
	
a = Circle(2)
surface = a.surface_circle()

print("원의 면적: {0}".format(cut_float(surface,2)))


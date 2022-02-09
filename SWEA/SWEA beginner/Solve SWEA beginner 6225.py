class Rectangle():
	
	def __init__(self,width,height):
		self.width = width
		self.height = height
		
	def cal_surface(self):
		return self.width * self.height

square = Rectangle(4,5)

print(f"사각형의 면적: {square.cal_surface()}")


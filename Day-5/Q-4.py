class Shape:
	def area(self):
		print("Area is not defined.")

	# def __init__(self, length, breadth):
	# 	self.length = length
	# 	self.breadth = breadth
		
	# def area(self, length, breadth):
	# 	return self.length * self.breadth

class circle(Shape):
	def __init__(self, radius):
		self.radius = radius
		self.radius = radius
	
	def area(self):
		return 3.14 * self.radius * self.radius
	
		
class Rectangle(Shape):
	def __init__(self, l, b):
		self.l = l
		self.b = b
		
	def area(self):
		return self.l * self.b

class Triangle(Shape):
	def __init__(self, base, height):
		self.base = base
		self.height = height
	
	def area(self):
		return 0.5 * self.base * self.height
	

C = circle(7)
R = Rectangle(45, 7)
T= Triangle(4, 7)

print("Circle: ",C.area())
print("Rectangle: ",R.area())
print("Triangle: ",T.area())
		

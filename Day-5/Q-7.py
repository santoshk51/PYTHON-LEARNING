class Person:
	def __init__(self, name, age = None, address = None):
		self.name = name
		self.age = age
		self.address = address

	def display(self):
		print("Name:",self.name)
		if (self.age is not None):
			print("Age:",self.age)
		
		if (self.address is not None):
			print("Address:",self.address)
		
		print("------------")


p1 = Person("santosh",22,"jaitpur")
p2 = Person("Raju",20,"madhubani")

print("Person one:",p1.display())
print("Person Two:",p2.display())


	
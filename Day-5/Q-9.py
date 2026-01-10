class Herbivore:
	def __init__(self, name, clas):
		self.name = name
		self.clas = clas

	def m1(self):
		return self.name and self.clas
	
class Carnivore:
	def __init__(self, age):
		self.age = age

	def m2(self):
		return self.age
	
class Omnivore:
	def __init__(self, gender):
		self.gender = gender

	def m3(self):
			return self.gender
	
class Bear(Herbivore, Carnivore, Omnivore ):
	def __init__(self, name, clas, voice, age, gender):
		super().__init__(name, clas)
		Carnivore.__init__(self, age)
		Omnivore.__init__(self, gender)
		self.voice = voice

dog = Bear("Dog","Animal","bhoo",10, "male")

cat = Bear("cat", "Animal", "meow", 5, "male")

bird = Bear("parrot","bird","copy",2,"female")


print("Dog Properties:",dog.name,dog.clas,dog.voice,dog.gender,dog.gender)
print("--------------------------")
print("Cat properties:",cat.name,cat.voice)
print("--------------------------")
print("Birds properties:",bird.name,bird.voice,bird.age,bird.gender)
print("--------------------------")

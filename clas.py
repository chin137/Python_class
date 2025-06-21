#Basic implementation of class with  an instance method

class Animal:
#Class attributes	
	count = 0
	def __init__(self,name,age):


#Example of a class method
	@classmethod
	def eat(cls):
		return "All animals eat, my friend"		

#Instance attributes		
		self.name = name
		self.age = age
		Animal.count = Animal.count + 1
	def __repr__(self):
		return f"He is {self.name} and {self.age}"	
#Example of an instance method		
	def play(self):
		return f"Hey, {self.name} is  playing now"




a1 = Animal("Masti",3)	
a2 = Animal("Reyu",2)
print(a1)
print(a2)
print(Animal.count)
print(a1.eat())
print(a2.eat())
		
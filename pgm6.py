#Concept: Use of del function to delete attributes of an object and an object itself
class Person:
	def __init__(self,name,age):#This is the constructor of the class Person
		self.name = name;
		self.age = age;


p1 = Person("Suppandi",14)


print("\n Name of Person #1 is",p1.name)
print("\n age of a Person #1 is",p1.age)

print("\n *** Printing after deleting age attribute for p1*** ")
del p1.age # Deleting the age attribute for p1 object 
print("\n Name of Person #1 is",p1.name)


print("\n*** Printing after Deleting p1***")
del p1
print("\n Name of Person #1 is",p1.name)

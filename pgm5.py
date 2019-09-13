#Notice the use of "self". It is the first argument passed to any fuction.
class Person:
	def __init__(self,name,age):#This is the constructor of the class Person
		self.name = name;
		self.age = age;

#Two objects s1 and s2 are created. the __init__constructor is automatically called

p1 = Person("Suppandi",14)
p2 = Person("Ramu",12)

print("\n Name of Person #1 is",p1.name)
print("\n age of a Person #1 is",p1.age)

print("\n Name of Person #2 is",p2.name)
print("\n age of a Person #2 is",p2.age)

p2.age = 10 # Attributes of the subject can be modified like this. By default public

print("\n Modified Age of a Person #2 is",p2.age)

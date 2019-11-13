class Student:
	def __init__(self,name,age,marks):
		self.name=name
		self.age=age
		self.marks=marks
	def get_data(self):
		self.name=str(input("Enter The Name:"))
		self.age=int(input("Enter The Age:"))

		for i in range(0,3):
			self.marks.append(int(input("Enter The marks:")))
	def display(self):
		print("Name = ",self.name,"Age = ",self.age)
		print("Marks in 3 sub ",self.marks)
s=Student("",0,[])
s.get_data()
s.display()
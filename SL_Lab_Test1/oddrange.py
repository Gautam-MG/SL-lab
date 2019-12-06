def oddrange(num1,num2):
	l=[]

	for i in range(num1,num2):
		if i%2!=0:
			l.append(i)
	return(l)

num1=int(input("Enter starting Number :" ))
num2=int(input("Enter Ending Number: "))
print("The OddRange Number Between",num1,"and",num2,"is :",oddrange(num1,num2))
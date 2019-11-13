def AgeConvert(num):
	num = num.split("-")
	age = 2019 - int(num[2])


	if int(num[1]) >10:
		age = age - 1
	print(age)
AgeConvert(str(input("Enter Your DOB Like DD-MM-YYYY :\n")))

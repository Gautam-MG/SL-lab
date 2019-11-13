def hourmin(num):
	mn=num%60
	hr=int(num/60)

	print(hr, "hours",":",mn, "minutes")
hourmin(int(input("Enter The Number :")))

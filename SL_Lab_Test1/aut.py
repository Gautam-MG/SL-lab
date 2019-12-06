dict = {1:'Hydrogin',2:'Lithium',3:'Boran',4:'Helium'}

def AutomicDict():
	while True:
		num=int(input("Enter Automic value   Enter 0 to Exit"))
		if(num==0):
			break;
		else:
			nam=str(input("Enter The Name of an automic:"))
			dict.update({num:nam})
			print(dict)

	print("Number of Automic values:",len(dict))
	sea=str(input("Enter The Elements to search:"))

	flag=0;

	for i in dict:
		if(dict[i].lower()==sea.lower()):
			print("Search Found")
			print({i,dict[i]})
			flag=1
			break;
		if(flag!=1):
			print("Not Found")
AutomicDict()
def LettersAround(s):
	flag=True
	equal=0
	plus=0

	for i in range(0,len(s)):
		if(s[i] == '='):
			equal+=1
			continue
		elif(s[i] == '+'):
			plus+=1
			continue
		elif(s[i].isalpha()):
			if(s[i-1] == '+' and s[i+1] == '+'):
				continue
			else:
				flag==False
				break
	if(flag == True and equal>0 and plus > 0):
		print("Accepted")
	else:
		print("Rejected")
LettersAround(str(input("Enter A String :")))
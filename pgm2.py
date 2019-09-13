students= {'1ms17is100':'asha','1ms17is101':'ashok','1ms17is102':'rekha','1ms17is103':'suma'}
list= ["value1","value2","value3","value4"]
list2= []
j=0
#print stud names
for i in students:

	print("key is ",i,"value is ",students[i])
	list[j]=students[i]
	#list2[j]=i
	j=j+1

print (list)
#print(list2)
print (students.keys())
print (students.values())
print (students.items())

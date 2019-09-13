#[1A] write a pythom program to read in a list of elements.Create a new list that holds all the elements minus the duplicate files(use functions)

def dup(l1):
	l2 = []
	for n in l1:
		if n not in l2:
			l2.append(n)



	print(l2);
	return l2
l1=[1,2,3,4,5,5,5,6,3,2]
dup(l1);	
# or dup([1,2,3,4,5,5,5,6,3,2]);


#[2A]Write a python program to read in a list of numbers.Use one-line comprehensions of create a new list of even numbers.Create another list reversing the elements.
S=[x**2 for x in range(10)] #read elements to list
M=[x for x in S if x % 2 == 0]
M.reverse()
print(S);
print(M);


#[3A] Write a python program to count the frequency of words in a given file.
from collections import Counter
def word_count(fname):
	with open(fname) as f:
		return Counter(f.read().split())

print("Number of words in the file :",word_count("music2.txt"))

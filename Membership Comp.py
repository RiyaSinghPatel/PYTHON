#Write a function that takes 2 arrays and prints the members of the first array that are present in the second array. (HINT: use Membership
#Comprehension

Array = []
Array1 = []
Array2=[]

n= int(input("enter the elemnt"))
for i in range(0,n):
	element = int(input())
	Array.append(element)
print(Array)

m= int(input("enter the secound elemnt"))
for j in range(0,m):
	element1 = int(input())
	Array1.append(element1)
print(Array1)

def common(Array, Array1):
	for i in Array:
		if i in Array1:
			Array2.append(i)
	return Array2

print (common(Array, Array1))
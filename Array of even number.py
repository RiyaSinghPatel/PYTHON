#Write a function to take an array and return another array that contains the members of the first array that are even.



#define an array
array= []
array1=[]

n= int(input("enter the elemnt"))
for i in range(0,n):
	element = int(input())
	array.append(element)
print(array)

def even(array):
	for i in array:
		if i%2 ==0:
			array1.append(i)
	return array1

print(even(array))

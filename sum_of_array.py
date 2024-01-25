# sum of its elements

import array as arr
array1=[]
n= int(input("enter the elemnt"))
for i in range(0,n):
	element = int(input())
	array1.append(element)
print(array1)

sum=0
for i in array1:
    # print(i)
    sum+=i
print("sum of the array:", sum)
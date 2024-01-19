#How to Add Two Numbers in Python – Easy Programs


#one way
num = 3
num1 = 5
sum = num + num1
print("Sum of", num, "and", num1 , "is", sum)

#2nd ways
n= int(input("enter the  1st elemnt :" ))
n1= int(input("enter the  2st elemnt :" ))
n3 = n + n1
print("Sum of", n , "and", n1 , "is", n3)

#3rd Ways
def add(num1, num2):
    sum = num1 + num2
    return sum
print(add(3,1))

#4th Ways
num1 = 1
num2 = 5
import operator
sum = operator.add(num1,num2)
print("the sum of {0} and {1} is {2} :" .format(num1,num2,sum))


#5th way
add_numbers = lambda x, y, c: x + y + c
num1 = 1
num2 = 2
num3 = 5
result = add_numbers(num1, num2, num3)
print("The sum of", num1, "and", num2, "and", num3, "is", result)
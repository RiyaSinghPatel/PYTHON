# Ask for the user’s first name and display the output message Hello [First Name] . 

name= input("enter the name of the user: ")
print ("Hello", name)

# 002 Ask for the user’s first name and then ask for their surname and display the output message 
# Hello [First Name] [Surname]. 

fname= input("enter the name of the user: ")
Lname= input("enter the last name of the user: ")
print ("Hello", fname, Lname)


# 003 Write code that will display the joke “What do you call a bear with no teeth?” and on the next line display the answer
# “A gummy bear!” Try to create it using only one line of code. 

print ("What do you call a bear with no teeth?\n","A gummy bear!")

# Ask the user to enter two numbers. Add them together and display the answer as The total is [answer].

n1= int(input("enter the 1st no: "))
n2= int(input("enter the 2nd no: "))
n3=n1+n2
print("The total is: ", n3)

# 05 Ask the user to enter three numbers. Add together the first two numbers and then multiply this total by the third. Display the 
# answer as The answer is [answer]. 

n1 = int(input("Enter the 1st number: "))
n2 = int(input("Enter the 2nd number: "))
n3 = int(input("Enter the 3rd number: "))
n4 = (n1 + n2) * n3

print("The total is:", n4)

# 06 Ask how many slices of pizza the user started with and ask how many slices they have eaten. Work out how many slices they have left 
# and display the answer in a userfriendly format. 

s1 = int(input("enter the number of slice you had:"))
s2 = int(input("enter the number of slice you had:"))

print("Slices left",s1-s2)


# 007 Ask the user for their name and their age. Add 1 to their age and display the output [Name] next birthday you 
# will be [new age].

s1 = input("Please enter your name:")
s2 = int(input("Please enter your age:"))
print(s1, "next birthday you will be", s2+1)

# 008 Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and
#  show how much each person must pay

s1 = int(input("Total Price of the bill:"))
s2 = int(input("Please enter no of diners:"))
print("Everyone has to pay:", s1/s2)

# 009 Write a program that will ask for a number of days and then will show how many hours, minutes and seconds are in that number of 
# days. 

s1 = int(input("Please enter the number of days:"))

h=s1*24
m= h*60
s=m*60
print(f"in {s1} days {h} hours",m, "min", s, "sec")

# 10 There are 2,204 pounds in a kilogram. Ask the user to enter a weight in kilograms and convert it to pounds.
s1 = int(input("enter the weight in kg:"))
con=s1*2204
print("weight in pound:",con)

# 011 Task the user to enter a number over 100 and then enter a number under 10 and tell them how many times the smaller number 
# goes into the larger number in a user-friendly format. 

s1 = int(input("enter over 100:"))
s2 = int(input("enter over 10:"))
s3=s1//s2
print(f"{s1} is", s3, f"times of {s2}")




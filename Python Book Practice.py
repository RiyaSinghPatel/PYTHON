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

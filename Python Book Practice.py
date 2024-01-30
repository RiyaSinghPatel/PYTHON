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


#**************************************BASIC - iF-ELSE QUESTION***********************************************

# 012 Ask for two numbers. If the first one is larger than the second, display the second number first and then the first 
# number, otherwise show the first number first and then the second. 


n1= int(input("enter the first number:"))
n2= int(input("enter the secound number:"))
if n1<n2:
    print(f"{n2} is greater than {n1}")
else:
     print(f"{n1} is greater than {n2}")

# 013 Ask the user to enter a number that is under 20. If they enter a number that is 20 or more, display the message “Too high”, 
# otherwise display “Thank you”.
     
n1= int(input("enter the number:"))
if n1 < 20:
    print("thankyou!")
elif n1==20 or n1>20:
         print("too high!")


# 14 Ask the user to enter a number between 10 and 20 (inclusive). If they enter a number within this range, display the message “Thank 
# you”, otherwise display the message “Incorrect answer”. 
         
n1= int(input("enter the number between 10 and 20:"))
if n1>= 10 and n1 <= 20:
      print("thankyou")
else:
      print("incorrect ans")

# 15 Ask the user to enter their favourite colour. If they enter “red”, “RED” or “Red” display the message “I like red too”,
# otherwise display the message “I don’t like [colour], I prefer red”. 
      
n1=input("enter the color:")

if n1.lower() == "red":
    print(f"I like this color {n1.lower()}")
else:
    print(f"I dont like this {n1} color")

# 016 Ask the user if it is raining and convert their answer to lower case so it doesn’t matter what case they type it in. 
# If they answer “yes”, ask if it is windy. If they answer “yes” to this second question, display the answer “It is too windy 
# for an umbrella”, otherwise display the message “Take an umbrella”. If they did not answer yes to the first question,
# display the answer “Enjoy your day”. 



n1=input("if it is raining")
n1_l = n1.lower()
if n1_l == "yes":
     n2=input("is it windy:")
     n2_l = n2.lower()
     if n2_l == "yes":
          print("It is too windy for an umbrella")
     else:
          print("Take an umbrella")
else:
     print("enjoy your day")


# 17 Ask the user’s age. If they are 18 or over, display the message “You can vote”, if they are aged 17, display the 
# message “You can learn to drive”, if they are 16, display the message “You can buy a lottery ticket”, if they are 
# under 16, display the message “You can go Trickor-Treating”.

age = int(input("Please enter your age: "))

if age >= 18:
    print("You can vote.")
elif age == 17:
    print("You can learn to drive.")
elif age == 16:
    print("You can buy a lottery ticket.")
else:
    print("You can go trick-or-treating.")


# 018 Ask the user to enter a number. If it is under 10, display the message “Too low”, if their number is 
# between 10 and 20, display “Correct”, otherwise display “Too high”
    
num = int(input("Please enter number: "))
if num<10:
     print("too low")
elif num > 10 and num < 20:
     print("correct")
else:
     print("too high")

# 19 Ask the user to enter 1, 2 or 3. If they enter a 1, display the message “Thank you”, if they enter a 2, display 
# “Well done”, if they enter a 3, display “Correct”. If they enter anything else, display “Error message”.
     

num = int(input("Please enter number: "))

if num == 1:
    print("thankyou")
elif num == 2:
    print("Well done")
elif num == 3:
    print("correct")
else:
    print("error messsage")


#***************************************BASIC - STRING question***********************************

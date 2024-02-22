# Write a program that takes two numbers as input from the user and then  prints the sum of these numbers.
def sum(a, b):
    a=int(input("enter first number:"))
    b=int(input("enter secound number:"))
    return a+b

add=sum(1,3)
print("sum of the number", add)

# Write a Program that takes Length and Breadth as input from user and
# print the Area of Rectangle.
# The formula for calculating the area of a rectangle is:
# Area = length × width

def rectangle(l, b):
   return l*b
a=int(input("lenght of rectangle:"))
b=int(input("breath of rectangle:"))

print("area of rectangle:", rectangle(a,b))

# Ask 3 numbers from User and Calculate the Average.

def avg(i,j,k):
    return (a+b+c)/2

a=int(input("enter 1 number:"))
b=int(input("enter 2 number:"))
c=int(input("enter 3 number:"))
print("enter the average of all the numbers", avg(a,b,c))

# Calculate sum of 5 subjects and Find percentage.
def add(subject):
    add = sum(subjects)
    percentage = add / (500) * 100
    return percentage

subjects = [85, 90, 78, 95, 88]
print("percent",add(subjects))

# Ask marks in 5 subjects and calculate Total Marks and Find percentage.
def sum(a,b,c,d,e):
    add = a+b+c+d+e
    cent= add / (500) * 100
    return cent
    
a=int(input("enter first number:"))
b=int(input("enter secound number:"))
c=int(input("enter first number:"))
d=int(input("enter secound number:"))
e=int(input("enter first number:"))
per = sum(a,b,c,d,e)
print("percent",per)

# 6. Calculate Area of Square by taking Length from User.
a=int(input("enter length of the square:"))
square = a**2
print("area of the square",square)


# Ask number of games played in a tournament. Ask the user number of
# games won and number of games loss. Calculate number of tie and total
# # Points. (1 win= 4 points, 1 tie =2 points)

a=int(input("games played in the tournament:"))
b=int(input("enter no of games won:"))
c=int(input("enter no of games loss:"))

games_tied = a - (b + c)
# Calculating total points
total_points = (b * 4) + (2 * 2)
print(f"Total points scored is {total_points}")
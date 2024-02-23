// # 1. Take two numbers as input from User and print which one is greater or
// # are they equal.

a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
if a > b:
    print("  greater", a)
elif b>a:
    print("greater", b)
else:
    print("both are equal")

// # 3. Take Salary as input from User and Update the salary of an employee
// # a. salary less than 10,000, 5 % increment
// # b. salary between 10,000 and 20, 000, 10 % increment
// # c. salary between 20,000 and 50,000, 15 % increment
// # d. salary more than 50,000, 20 % increment


sal = int(input("enter the salary:"))

if sal<10000:
    print ("salary:", (sal+(sal+0.05)))
elif sal>10000 and sal<20000:
    print ("salary:", (sal+(sal+0.1)))

elif sal>20000 and sal<50000:
    print ("salary:", (sal+(sal+0.15)))
elif sal>50000:
    print("sal", (sal+(sal+.2)))


// # 4. Ask the number from User and print whether the number is Odd or Even.
a=int(input("enter the number:"))
if a%2==0:
    print("number id even")
else:
   print("number is odd")


// # 6. A student will not be allowed to sit in exam if his/her attendance is less
// # than 75%.
// # a. Take following input from user
// # i. Number of classes held
// # ii. Number of classes attended.
// # b. Print percentage of class attended
// # c. Print Is student is allowed to sit in exam or not.


a=int(input("enter the number of class held:"))
b=int(input("enter the number of class attended:"))

percent = (b/a)*100
print ("percent of class attended:", percent)
if percent > 75:
    print("you are allow to sit")
else:
    print("not allowed")


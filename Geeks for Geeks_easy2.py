
#1st way   
def max(num,num1):
    if num>num1:
        return num
    else:
        return num1
    
num = input("enter the 1st :")
num1 = input("enter the 2nd :")
print(max(num,num1))
#===============================================================
#2nd way #by function
n = input("enter the 1st value:")
n1 = input("enter the 2nd value:")

if(n<n1):
    print(f"the value {n1} is greater than {n}")
else:
    print(f"value {n} is greater")
#===============================================================
#using Max funtion
num = input("enter the value1:")
num1 = input("enter the value2 :")
maximum = max(num,num1)
print("this is max value:", maximum)

#===============================================================
#using lambda function
x = input("enter the value1:")
y = input("enter the value2 :")
Max_value=lambda x,y: x if x>y else y
print("max value is: ", Max_value(x,y))

#===============================================================
#using list comprehension
x = input("enter the value1:")
y = input("enter the value2 :")
max=(x if x>y else y)
print("this is the max value:", max)

#===============================================================
#using short function
x = input("enter the value1:")
y = input("enter the value2 :")
max=[x,y]
max.sort()
print(max[1])



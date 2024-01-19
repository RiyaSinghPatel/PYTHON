#Python Program to Find the Factorial of a Number


def fact(num):
    if num == 0 or num ==1:
        return 1
    else:
         return num * fact(num - 1)
    
num = int(input("enter the number to find the factorial of:"))
print(f"factorial of {num} is :", fact(num) )


#=============================================
 
n = int(input("enter the number to find the factorial of:"))

def fact(n):
    if n < 0:
         return 0
    elif n == 0 or n==1:
        return 1
    else:
        fact1 = 1
        while n > 1:
            fact1 = fact1 * n
            n= n-1
        return fact1
print("factorial:", fact(n))  


n=int(input("enter the number:"))
order= len(str(n))
s=n;
sum= 0
while(n>0):
    r=n%10
    sum+=r**order
    n=n//10
if(sum==s):
    print("this is armstrong number")

else:
    print("this is not armstrong number")
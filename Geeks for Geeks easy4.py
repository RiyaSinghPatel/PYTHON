#Python Program for Simple Interest

p= int(input("enter the Principal amount: "))
t= int(input("enter the time: "))
r= int(input("enter the rate: "))

SI= p*t*r/100
print("simple interest: ", SI)

#============================================================
#2nd way
def sim(p,r,t):
    print("Enter the principle:,p ")
    print("Enter the time: ",t)
    print("Enter the rate: ",r)
    return p*r*t/100
print("simple interest:", sim(125,5,8))

import random
nump=random.randint(1000, 9999)
print(nump) #1444
n=int(input("enter the number to guess:"))
while n!=10: #press 10 to quit
    num=nump  #1234
    cor=0
    while num%10:
        numc=num%10 #4
        nc=n%10 #4
        num=num//10 #144
        n=n//10 #123
        if numc==nc:
            cor=cor+1
    if cor == 4:
        print("congrats")
        break
    else:
        print ("%d you guessed right" %cor)
        n=int(input("enter the number to guess:"))
else:
    print("quit")
        
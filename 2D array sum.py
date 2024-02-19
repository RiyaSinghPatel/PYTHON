r=int(input("enter the number of rows:")) 
c=int(input("enter the number of colum:"))
x=[]
val=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j,int(input("enter the %d*%d element:")))
    x.insert(i,val)
    val=[]    

y=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j,int(input("enter the %d*%d element:")))
    y.insert(i,val)
    val=[]   

sum=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j, x[i][j] + y[i][j])
    sum.insert(i,val)
    val=[] 
print(sum)  
print(sum[0][1])

import array as arr
array=[]

a=int(input("enter the array:" ))

for i in range(a):
    element= int(input())
    array.append(element)


def max_array(a1, n):
    max=a1[0]
    for i in range(n):
        if a1[i] >max:
              max= a1[i]
    return max

print(f"The maximum element in the array is: {max_array(array,a)}")


#2nd way
array=[]
n=int(input("enter the array:"))
for i in range(0,n):
     element = int(input())
     array.append(element)
print(array)

def large(arr,n):
     arr.sort()
     return arr[n-1]
print(large(array,n))


















            
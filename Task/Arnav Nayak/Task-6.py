a=[]
b=[]
count=0
n=int(input("Enter the number of elements in the array: "))
for i in range(0,n):
    element=int(input("Enter the elements: "))
    a.append(element)
print("The array is: ",a)    
for i in range(0, n):
    fact = 0  
    for j in range(1, a[i] + 1): 
        if a[i] % j == 0:
            fact += 1 
    if fact == 2:  
        b.append(a[i])
        count += 1 
print("\n The prime numbers in the array are: ",b)          
small=b[0]
large=b[0]
for i in range(0,count):
    if(small>b[i]):
        small=b[i]
for i in range(0,count):
    if(large<b[i]):
        large=b[i]
print("\nLargest prime number in the array is: ",large)
print("\nSmallest prime number in the array is: ",small) 
difference=large-small 
print("\nThe difference between the largest and the smallest prime number in the array given by you is: ",difference)                           
a=input("Enter the elements of the list: ")
lst=a.split(" ")
primelst=[]
print(sorted(lst))
lst1=sorted(lst)
for i in lst1:
    c=0
    for j in range(1,int(i)+1):
        if(int(i)%j==0):
            c=c+1
    if(c==2):
        primelst.append(i)
print("The prime numbers in the list are", primelst)
b=int(primelst[-1])-int(primelst[0])
print("The difference between the largest and smallest prime number is ", b)
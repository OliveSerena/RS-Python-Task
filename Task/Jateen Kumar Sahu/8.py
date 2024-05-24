m=input("Enter a list:")
b=list(m)
D={}
for i in b:
    if i in D:
        D[i]+=1
    else:
        D[i]=1

print (D)
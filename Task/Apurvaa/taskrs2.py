strng=input("Enter a word: ")
strg=strng.replace(" ","")
lst=[]
for i in strg:
    lst.append(i)
b=set()
for i in lst:
    b.add(i)
c=[]
for j in b:
    c.append(j)
for i in c:
    count=0
    for j in strg:
        if(i==j):
         count=count+1
        else:
            continue
    print(i, "---", count)
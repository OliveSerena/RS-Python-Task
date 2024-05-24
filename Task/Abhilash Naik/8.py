from collections import Counter
l=[]
n=int(input("enter the no of element in l: ",))
for i in range(0,n):
    elem=(input())
    l.append(elem)
print(l)
lc=Counter(l)
for i in lc:
        print(i + "->" + str(lc[i]),end="\n")
print(dict(Counter(l)))
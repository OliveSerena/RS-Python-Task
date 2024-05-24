from collections import Counter
s=str(input("enter a string:"))
d = sorted(s)
e = Counter(d)
for i in e:
    if i==" ":
        print("\n")
    else:    
        print(i + "->" + str(e[i]),end="\n")
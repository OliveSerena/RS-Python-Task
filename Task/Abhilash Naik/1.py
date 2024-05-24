s=str(input("enter a word:"))
t=str(input("enter the socond word:"))
print(f'Input:s="{s}", t = "{t}"')
s1=sorted(s)
t1=sorted(t)
if s1==t1:
    print("output:true")
else:
    print("output:false")


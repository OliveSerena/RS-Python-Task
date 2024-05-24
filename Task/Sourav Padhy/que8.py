num1=[1,2,3,2,4,1,5]
dict={}
for num in num1:
    if num in dict:
        dict[num]=dict[num]+1
    else:
        dict[num]=1

print(dict)
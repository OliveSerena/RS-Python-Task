string = "assAsinATion"
list = []
for i in range(len(string)): 
    
    list.append(string[i])
list.sort()
print("In lexicographical order",list)

for j in range(len(list)):
   print(list[j],list.count(list[j]))
 
    
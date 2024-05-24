s = "anagram"
sum = 0
length = len(s)

for i in range(0,length):


 sum +=  ord(s[i])

#print(sum)

#for dusra string

t ="nagaram"
sum1=0
length1 = len(t)

for j in range(0,length1):
 
    sum1 += ord(t[j])

#print(sum1)


if sum == sum1:
   print("Both wordas are anagram")
else:
    print("Both words are not anagram")




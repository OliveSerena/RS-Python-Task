##QUESTION NO.2
word = "Robotics Society"
s = list(word)
s.sort()
print(s)

frequency={}
for char in s:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1
for char,freq in frequency.items():
    if char!='':
        print("{} -> {}".format(char,freq))
        

def IsAnagram(s,t):
    s = s.lower()
    t = t.lower()
    count = 0
    if (len(s)!=len(t)):
      return False
    for i in range(0, len(s)):
        for j in range(0, len(t)):
            if(s[i] == t[j]):
                count += 1
    if (count == len(s)):
        return (True)
    else:
        return (False)    
s=input("Enter the first string: ")
t=input("Enter the second string: ")   
print(IsAnagram(s,t))    
def isAnagram(str_s,str_t):
    if sorted(str_s) == sorted(str_t):
     return True
    else: 
     return False
str_s = "anagram"
str_t = "nagaram"
print(isAnagram(str_s, str_t))
str_s = "rat"
str_t = "car"
print(isAnagram(str_s, str_t))



a=input("Enter a word: ")
b=input("Enter another word:")
c=len(a)
d=len(b)
if(c!=d):
   print("not anagram")
else:
   if(sorted(a)==sorted(b)):
      print("These are anagram.")
   else:
      print("Not anagram.")
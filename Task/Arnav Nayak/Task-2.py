def CharacterFrequency(s):
    frequency={}
    for char in s:
        if(char!=' '):
            frequency[char]=frequency.get(char,0)+1
    character=sorted(frequency.keys())
    for char in character:  
        print(char + "->", frequency[char])    
s=input("Enter the string to check character frequency: ")
CharacterFrequency(s)        

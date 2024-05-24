def Frequency(List):
    frequency={}
    for element in list:
        if element in frequency:
            frequency[element]+=1
        else:
            frequency[element]=1    
    return frequency
list=input("Enter the elements of the list: ").split()
frequency=Frequency(list)
print("Frequency of each element: ")
print(frequency)
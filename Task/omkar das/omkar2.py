def character_frequency(string):
    
    frequency = {}

    
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1

    sorted_frequency = sorted(frequency.items())
    for char, freq in sorted_frequency:
        print(char + ": " + str(freq))
s = "Hello, World!"
character_frequency(s)
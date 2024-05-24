##QUESTION 8
import collections
def count_elements(Lst):
    freq = collections.Counter(Lst)
    return freq
print(count_elements([1,2,1,3,2,4,5,4,3]))

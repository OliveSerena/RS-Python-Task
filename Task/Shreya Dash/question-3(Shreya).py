def plusOne(digits):
   i = 1
   for n in range(len(digits) -1, -1, -1):
             digits[n] <= 10
             digits[n] += 1
   if digits[n] != 0:
               digits = [n] + digits
               return digits
            
digits1 = [1,2,3]
print("Output:", plusOne(digits1))
digits2 = [4,3,2,1]
print("Output:", plusOne(digits2))
digits3 = [9]
print("Output:", plusOne(digits3))
digits = [1,3,9]

length=len(digits)

number = digits[length-1]

digits[length-1]=number+1


if digits[length-1]<10:

        print(digits)

elif number == 9 and length ==1 :
        digits=[1,0]
        print(digits)

else:
        digits[length-1]=0
        digits[length-2]=digits[length-2]+1
        print(digits)
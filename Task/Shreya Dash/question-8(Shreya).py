m = input("Enter a list: ")
Dctnry = {}

for i in m:
    Dctnry[i] = Dctnry.get(i, 0) + 1

    print(Dctnry)
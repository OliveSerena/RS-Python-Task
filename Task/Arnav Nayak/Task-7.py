import math
def primeFactors(n):
    factors = set() 
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors
def payment(mrp):
    primefactors = primeFactors(mrp)
    return mrp - sum(primefactors)
print("Welcome! This program calculates how much money Roy has to pay for each product.")
print("Please enter the number of products they bought:")
N = int(input())

print("Now, enter the MRP of each product one by one:")

for i in range(N):
    R = int(input())
    print("For product", i+1, "Roy has to pay:", payment(R))
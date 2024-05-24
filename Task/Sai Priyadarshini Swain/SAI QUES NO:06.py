##QUESTION 6
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

N = int(input())
A = list(map(int, input().split()))
primes = [x for x in A if is_prime(x)]

if len(primes) < 2:
    print(1)
else:
    print(max(primes) - min(primes))

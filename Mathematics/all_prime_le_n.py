import math
from is_prime import is_prime
def sieve(n):
    prime = [True] * (n+1)
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime(i):
            for j in range(i*i, n + 1, i):
                prime[j] = False
    for i in range(2, n+1):
        if prime[i]:
            print(i)
def all_primes(n):
    if n >=2:
        print(2)
    if n >= 3:
        print(3)
    for i in range(5, n + 1, 6):
        if is_prime((i)):
            print(i)
        if is_prime((i + 2)) and i + 2 <= n:
            print(i+2)

if __name__ == "__main__":
    n = int(input("What`s n? "))
    # all_primes(n)
    sieve(n)
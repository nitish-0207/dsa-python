import math
def divisors(n):
    ...
    sq_n = int(math.sqrt(n))
    for i in range(1,sq_n + 1):
        if i == sq_n:
            print(i)
        elif n % i == 0:
            print(i, n // i,end=' ')

if __name__ == "__main__":
    n = int(input("What`s n? "))
    divisors(n)
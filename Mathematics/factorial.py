import sys
def factorial(n):
    if(n < 0):
        sys.exit("Enter a non negative integer")
    res = 1
    while n > 0:
        res = res * n
        n -= 1
    return res
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    fact = factorial(num)
    print(f"Factorial of {num} is {fact}")
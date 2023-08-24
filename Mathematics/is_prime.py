import sys, math
def is_prime_optimize(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True
def is_prime(n):
   
    # print("sqrt:", int(math.sqrt(n)))
    for i in range(2,int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    try:
        n = int(input("Enter number: "))
    except:
        sys.exit("Enter a valid integer")
    
    if is_prime_optimize(n):
        print("Yes")
    else:
        print("No")
    # Checking both function giving same result or not
    for i in range(1,100):
        if is_prime(i) != is_prime_optimize(i):
            print("Something wrong...")
        print(is_prime(i) == is_prime_optimize(i))
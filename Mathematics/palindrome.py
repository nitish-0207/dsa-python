
def reverse(n):
    # 1234 = 4321
    i = 0
    rev = 0
    while n > 0:
        rev = (rev * 10) + (n % 10)
        n //= 10
    return rev
def is_palindrome(n):
    return n == reverse(n)
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(is_palindrome(num))

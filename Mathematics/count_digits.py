def count_digits(n):
    no_of_dig = 0
    if n == 0:
        return 1 
    while n > 0:
        no_of_dig += 1
        n //= 10
    return no_of_dig

def main():
    # print("Hello")
    num = int(input("Enter a number: "))
    digits = count_digits(num)
    print(f"no. of digits in {num} = {digits}")


if __name__ == "__main__":
    main()
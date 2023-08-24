def hcf(a,b):
    if a > b:
        a,b = b,a
    if b % a == 0:
        return a
    return hcf(b % a, b)


if __name__ == "__main__":
    a,b = input().split(" ")
    a = int(a)
    b = int(b)
    print(hcf(a,b))
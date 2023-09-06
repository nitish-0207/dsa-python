def sum_natural(n,sum):
    if n == 0:
        return sum
    sum_natural(n-1,sum + n)
    print(sum)
    return sum

if __name__ == "__main__":
    n = int(input())
    sum = 0
    ans = sum_natural(n,sum)
    print(ans)
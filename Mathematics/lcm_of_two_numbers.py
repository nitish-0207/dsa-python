from hcf_of_two_numbers import hcf
def lcm(a,b):
    return a * b // hcf(a,b)

if __name__ == "__main__":
    ans = lcm(40,12)
    print(ans)
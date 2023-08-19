#################################################################################
# i/p: n = 5   ==> o/p: 1 since factorial of 5 is 120 and has 1 trailing zero   #
# i/p: n = 10  ==> o/p: 2                                                       #
# i/p: n = 100 ==> o/p: 24                                                      #
#################################################################################
def trail_zero(n):
    ans = 0
    while n // 5 > 0:
        ans += (n // 5)
        n = n // 5
    return ans
        
if __name__ == "__main__":
    num = int(input("Enter a number: "))
    num_zeros_end = trail_zero(num)
    print(f"Number of trailing zeros in factorial of {num} is {num_zeros_end}")
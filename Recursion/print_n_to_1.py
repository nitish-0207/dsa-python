# IP: n = 5, OP: 5,4,3,2,1
def n_to_one(n):
    if n == 1:
        print(1,end='')
        return
    print(n, end=',')
    n_to_one(n-1)
if __name__ == "__main__":
    n = int(input())
    n_to_one(n)
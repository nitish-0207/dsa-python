# IP: n = 5, OP: 1,2,3,4,5
def n_to_one(n, l):
    if n == 1:
        l.append(n)
        return
    n_to_one(n-1, l)
    l.append(n)
    return l
    
if __name__ == "__main__":
    n = int(input())
    l = []
    n_to_one(n, l)
    for i in range(len(l) - 1):
        print(l[i], end='')
    print(l[-1], end='')

    print((for i in l: i)

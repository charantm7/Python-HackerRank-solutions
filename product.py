from itertools import product

if __name__ == '__main__':

    i,j = list(map(int, input().split())), list(map(int, input().split()))

    res = product(i,j)
    print(*res)

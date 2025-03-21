from itertools import combinations


if __name__ == '__main__':

    i,j = input().split()
    j = int(j)

    i = (''.join(sorted(i)))
    for k in range(1,j+1):
        for k in combinations(i,k):
            print(''.join(k))
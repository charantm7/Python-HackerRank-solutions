from itertools import permutations


if __name__ == '__main__':

    i,j = input().split()
    j = int(j)

    i = (''.join(sorted(i)))

    for k in permutations(i,j):
        print(''.join(k))
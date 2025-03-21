from itertools import combinations_with_replacement


if __name__ == '__main__':
    
    i = input().split()
    j = int(input())
    
    i = (''.join(sorted(i)))
    
    
    
        
    for comb in combinations_with_replacement(i,j):
        print(''.join(comb))
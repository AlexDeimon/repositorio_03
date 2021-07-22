from itertools import combinations
s,n = input().split()
for l in range(1,int(n)+1):
    for c in combinations (sorted(s),l):
        print(''.join(c))
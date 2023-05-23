# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations
word, r = list(input().split())
arr =sorted([i for i in word])
r = int(r)


for i in range(1, r+1):
    comb = list(combinations(arr, i))
    for i in comb:
        print("".join(i))

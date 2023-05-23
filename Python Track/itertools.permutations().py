# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
word, r = list(input().split())
r = int(r)
arr = sorted(list(permutations(word, r)))
for i in range(len(arr)):
    for j in range(r):
        print(arr[i][j], end="")
    print("")

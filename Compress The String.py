# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import groupby
string = input()
arr = [x for x in string]
groups = groupby(arr)

for key, group in groups:
    print((len(list(group)), int(key)), end=" ")

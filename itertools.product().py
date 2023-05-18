from itertools import product

A = list(set(map(int, input().split())))
B = list(set(map(int, input().split())))
t = tuple((product(A, B)))
for i in t:
    print(i, end=" ")

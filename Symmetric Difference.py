# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
N = set(input().split())
m = int(input())
M = set(input().split())

a = list(M.difference(N))
b = list(N.difference(M))

arr = sorted(list(map(int, a + b)))
for i in arr:
    print(i)

from collections import defaultdict
n, m = list(map(int, input().split()))

groupA = defaultdict(list)
for i in range(1, n+1):
    a = input()
    groupA[a].append(i)

for i in range(m):
    a = input()
    if a in groupA:
        print(" ".join(map(str,groupA[a])))
    else:
        print("-1")

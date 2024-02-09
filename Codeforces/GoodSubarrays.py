import sys
import math 
from collections import defaultdict
from collections import Counter
def I(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()
def SL(): return list(sys.stdin.readline().strip())
def SIL(): return sorted(list(map(int, sys.stdin.readline().strip().split())))

def solve():
    n = I()
    a = list(map(int, SL()))
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    count = defaultdict(int)
    ans = 0
    for i in range(n):
        count[prefix[i] - i + 1] += 1
        ans += count[prefix[i + 1] - i]
        
    print(ans)
    # print(count)
    # print(p)
    # print(a)
    
# solve()
t = I()
for g in range(t):
    solve()
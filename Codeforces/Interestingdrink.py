import sys
import math 
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def I(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = I()
    a = sorted(IL())
    q = I()
    arr = []
    for _ in range(q):
        print(bisect_right(a, I()))
    
# solve()
for _ in range(1):
    solve()
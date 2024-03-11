import sys
import math 
from collections import defaultdict, Counter, deque
from bisect import bisect_left, bisect_right
def I(): return int(sys.stdin.readline().strip())
def IL(): return list(map(int, sys.stdin.readline().strip().split()))
def S(): return sys.stdin.readline().strip()

def solve():
    n = I()
    position = IL()
    speed = IL()
    p_s = sorted([(position[i], speed[i]) for i in range(n)])
    def is_valid_time(time):
        minn, maxx = p_s[0][0] - (time * p_s[0][1]), p_s[0][0] + (time * p_s[0][1])

        for i in range(1, len(p_s)):
            cur_minn = p_s[i][0] - (time * p_s[i][1])
            cur_maxx = p_s[i][0] + (time * p_s[i][1])
            
            if cur_minn <= maxx:
                maxx = min(maxx, cur_maxx)
            else:
                return False
            
        return True
    
    l, r = 0, max(position) 
    # print(r)
    while l + 1e-7 < r:
        mid = (l + r) / 2
        # print(mid)
        if is_valid_time(mid):
            r = mid
        else:
            l = mid 
    print(r)


    

for _ in range(1):
    solve()
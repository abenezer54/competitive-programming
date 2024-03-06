class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        total = sum(weights)
        weights.append(inf)
        
        def day_calculator(capacity):
            cur_days = cur = 0
            for i, w in enumerate(weights):
                cur += w
                if i < len(weights) - 1 and capacity < w:
                    return inf
                if cur > capacity:
                    cur_days += 1
                    cur = w
 
            return cur_days
            
        l, r = 1, total
        while l + 1 < r:            
            mid = (l + r) // 2
            if day_calculator(mid) <= days:
                r = mid
            else:
                l = mid
        return r
        
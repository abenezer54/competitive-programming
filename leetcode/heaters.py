class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def is_valid(radius):
            ptr = 0
            for heater in heaters:
                while ptr < len(houses) and (heater - radius) <= houses[ptr] <= heater + radius:
                    ptr += 1
            return ptr == len(houses)

        l, r = -1, max(max(houses), max(heaters))
        while l + 1 < r:
            mid = (l + r) // 2

            if is_valid(mid):
                r = mid
            else:
                l = mid
        return r
        
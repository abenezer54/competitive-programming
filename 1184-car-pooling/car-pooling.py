class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        maxValue = max(trips,key=lambda x:x[-1])[-1]
        print(maxValue)
        prefix = [0] * (maxValue + 2)
        for trip in trips:
            prefix[trip[1]] += trip[0]
            prefix[trip[2]] -= trip[0]
        summ = 0
        for num in prefix:
            summ += num
            if summ > capacity:
                return False
        
        return True
        
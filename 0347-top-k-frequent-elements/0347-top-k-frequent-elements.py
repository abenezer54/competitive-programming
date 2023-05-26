class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        dic = defaultdict(list)
        minn = min(nums)
        maxx = max(nums)
        r  = maxx - minn + 1
        counter = [0]* r
        for i in range(len(nums)):
            counter[nums[i] - minn] += 1 
        for i in range(len(counter)):
            dic[counter[i]].append(i + minn)
            
        counter = list(set(counter))
        ans = []
        i = 0
        while i < k:
            ans.extend(dic[max(counter)])
            if len(counter) >= 1:
                i += len(dic[max(counter)])
            else:
                break
            counter.remove(max(counter))
            
        return ans
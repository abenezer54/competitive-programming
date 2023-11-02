class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i + 1] = prefix[i] + nums[i]
        
        ans = []  
        for maxx in queries:
            print(maxx)
            found = False
            for i in range(1, len(prefix)):
                if prefix[i] > maxx:
                    ans.append(i - 1)
                    found = True
                    break
            if not found:
                ans.append(len(prefix) - 1)

        return ans